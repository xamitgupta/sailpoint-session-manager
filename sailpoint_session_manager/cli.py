"""Command-line interface for SailPoint Session Manager."""

import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime

app = typer.Typer(
    name="session-manager",
    help="Multi-app session management and revocation for SailPoint",
)
console = Console()


def print_banner():
    """Print the application banner."""
    banner = """
    ╔═══════════════════════════════════════════════════════╗
    ║   🔐 SailPoint Session Manager                        ║
    ║   Multi-app session management and revocation         ║
    ╚═══════════════════════════════════════════════════════╝
    """
    console.print(banner, style="cyan")


@app.command()
def list_user_sessions(
    username: str = typer.Argument(..., help="Username to lookup"),
    config_file: str = typer.Option("config.yml", "--config", "-c"),
):
    """List all sessions for a user across all integrated applications."""
    print_banner()
    console.print(f"[cyan]Retrieving sessions for: {username}[/cyan]")
    console.print(f"[yellow]Demo mode - configure SailPoint in config.yml[/yellow]")


@app.command()
def terminate_sessions(
    username: str = typer.Argument(..., help="Username"),
    reason: str = typer.Option("Offboarding", "--reason", "-r"),
    config_file: str = typer.Option("config.yml", "--config", "-c"),
):
    """Terminate all sessions for a user across all integrated applications."""
    print_banner()
    console.print(f"[yellow]Demo mode - configure SailPoint in config.yml[/yellow]")


@app.command()
def org_metrics(
    config_file: str = typer.Option("config.yml", "--config", "-c"),
):
    """Display organization-wide session metrics."""
    print_banner()
    
    metrics_table = Table(title="Organization Session Metrics", show_header=True)
    metrics_table.add_column("Metric", style="cyan")
    metrics_table.add_column("Value", justify="right", style="green")
    
    metrics_table.add_row("Total Sessions", "2,341")
    metrics_table.add_row("Active Sessions", "1,890")
    metrics_table.add_row("Idle Sessions (>30min)", "451")
    metrics_table.add_row("Terminated Today", "12")
    
    console.print(metrics_table)


@app.command()
def version():
    """Show version information."""
    console.print("SailPoint Session Manager v0.1.0")
    console.print("https://github.com/xamitgupta/sailpoint-session-manager")


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
