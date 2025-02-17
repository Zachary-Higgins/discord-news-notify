import logging
import os
import time
from rich.logging import RichHandler
from rich.progress import Progress, BarColumn, TimeRemainingColumn
from rich.console import Console

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%Y-%m-%d %H:%M:%S]",  # Custom timestamp format
    handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.setLevel(os.getenv("LOG_LEVEL", "DEBUG"))  # Default is DEBUG
console = Console()

def countdown(seconds: int):
   """Stylized countdown with a custom progress bar."""
   with Progress(
      "[bold cyan]{task.description}",  # Task description in cyan
      BarColumn(bar_width=None, style="magenta"),  # Magenta progress bar
      "[bold green]{task.percentage:.0f}% completed",
      TimeRemainingColumn(),  # Show estimated time remaining
   ) as progress:
      task = progress.add_task("⏳ Countdown...", total=seconds)
      for i in range(seconds, 0, -1):
         progress.update(task, completed=seconds - i)
         time.sleep(1)
      progress.update(task, completed=seconds)
   console.print("[bold green]✅ Countdown complete![/bold green]")
