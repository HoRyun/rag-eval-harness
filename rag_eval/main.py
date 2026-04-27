"""CLI entrypoint for rag-eval-harness."""

import typer

app = typer.Typer(help="Evaluate whether a local RAG API retrieves expected sources.")


@app.command()
def check() -> None:
    """Placeholder command for the initial project scaffold."""
    typer.echo("rag-eval-harness scaffold is ready.")
