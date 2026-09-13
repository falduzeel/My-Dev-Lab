import csv
import datetime as dt
import logging
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import List, Optional, Tuple

# Configure logging output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class EmailConfig:
    """Stores SMTP connection details and email credentials securely."""

    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        app_password: str
    ) -> None:
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.app_password = app_password


class QuoteManager:
    """Handles reading and selecting quotes from external files."""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def load_quotes(self) -> List[str]:
        """Reads quotes from a text file, returning a list of clean strings."""
        if not self.file_path.exists():
            logging.warning(f"File {self.file_path} not found. Using fallback quotes.")
            return [
                "The secret of getting ahead is getting started.",
                "It always seems impossible until it's done.",
                "Quality is not an act, it is a habit."
            ]

        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                quotes = [line.strip() for line in file if line.strip()]
            return quotes
        except OSError as error:
            logging.error(f"Error reading quotes file: {error}")
            return []

    def get_random_quote(self) -> Optional[str]:
        """Returns a random quote from the loaded list."""
        quotes = self.load_quotes()
        return random.choice(quotes) if quotes else None


class BirthdayManager:
    """Manages birthday records and checks for matches on current date."""

    def __init__(self, csv_path: Path) -> None:
        self.csv_path = csv_path

    def get_todays_birthdays(self, target_date: dt.datetime) -> List[Tuple[str, str]]:
        """Parses CSV file and returns list of tuples containing (name, email) for today's matches."""
        matched_recipients: List[Tuple[str, str]] = []

        if not self.csv_path.exists():
            logging.warning(f"Birthday CSV file not found at {self.csv_path}.")
            return matched_recipients

        try:
            with open(self.csv_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    month = int(row.get("month", 0))
                    day = int(row.get("day", 0))
                    if month == target_date.month and day == target_date.day:
                        matched_recipients.append((row["name"], row["email"]))
        except (KeyError, ValueError, OSError) as error:
            logging.error(f"Failed to process birthday CSV: {error}")

        return matched_recipients


class MailService:
    """Handles SMTP connection lifecycle and email dispatching."""

    def __init__(self, config: EmailConfig) -> None:
        self.config = config

    def send_email(self, recipient_email: str, subject: str, body_text: str) -> bool:
        """Constructs a MIME email message and sends it via encrypted TLS."""
        message = MIMEMultipart("alternative")
        message["From"] = self.config.sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body_text, "plain", "utf-8"))

        try:
            logging.info(f"Connecting to SMTP server {self.config.smtp_server}:{self.config.smtp_port}...")
            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port, timeout=15) as server:
                server.starttls()
                server.login(self.config.sender_email, self.config.app_password)
                server.sendmail(self.config.sender_email, recipient_email, message.as_string())
            logging.info(f"Email successfully delivered to {recipient_email}")
            return True
        except smtplib.SMTPAuthenticationError:
            logging.error("SMTP Authentication failed. Check your email address and app password.")
        except smtplib.SMTPException as error:
            logging.error(f"SMTP error occurred while sending email: {error}")
        except Exception as error:
            logging.error(f"Unexpected connection error: {error}")

        return False


class NotificationApp:
    """Main application orchestrator combining scheduled triggers, quotes, and birthday notifications."""

    def __init__(self, config: EmailConfig, quotes_path: Path, birthdays_path: Path) -> None:
        self.mail_service = MailService(config)
        self.quote_manager = QuoteManager(quotes_path)
        self.birthday_manager = BirthdayManager(birthdays_path)

    def run_daily_checks(self) -> None:
        """Executes scheduled checks for Monday motivation and birthday emails."""
        today = dt.datetime.now()
        logging.info(f"Running automated daily notification check for {today.strftime('%Y-%m-%d')}...")

        # Task 1: Check Monday Motivation (Weekday 0 = Monday)
        if today.weekday() == 0:
            logging.info("Today is Monday. Preparing motivational broadcast...")
            quote = self.quote_manager.get_random_quote()
            if quote:
                subject = "Weekly Motivation"
                body = f"Hello,\n\nHere is your quote for the week:\n\n\"{quote}\"\n\nHave a great week ahead!"
                self.mail_service.send_email(self.mail_service.config.sender_email, subject, body)

        # Task 2: Check Birthday Reminders
        todays_birthdays = self.birthday_manager.get_todays_birthdays(today)
        if todays_birthdays:
            logging.info(f"Found {len(todays_birthdays)} birthday(s) today!")
            for name, email in todays_birthdays:
                subject = f"Happy Birthday, {name}!"
                body = f"Dear {name},\n\nWishing you a wonderful birthday filled with joy and success!\n\nBest regards,"
                self.mail_service.send_email(email, subject, body)
        else:
            logging.info("No birthdays found for today.")


if __name__ == "__main__":
    # Define file paths using Pathlib
    BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()
    QUOTES_FILE = BASE_DIR / "quotes.txt"
    BIRTHDAYS_FILE = BASE_DIR / "birthdays.csv"

    # SMTP Configuration (Use Gmail App Passwords)
    config = EmailConfig(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        sender_email="your_email@gmail.com",
        app_password="your_16_digit_app_password"
    )

    # Instantiate and execute application
    app = NotificationApp(
        config=config,
        quotes_path=QUOTES_FILE,
        birthdays_path=BIRTHDAYS_FILE
    )
    app.run_daily_checks()
