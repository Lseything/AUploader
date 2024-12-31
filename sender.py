import os
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.box import ROUNDED

# Configurações
console = Console()

# Arte ASCII para "Install Packages"
INSTALL_PACKAGES_ASCII = """
[bold rgb(0,255,255)]
█████  ██████   █████   ██████ ██   ██  █████   ██████  ███████ ███████ 
██   ██ ██   ██ ██   ██ ██      ██  ██  ██   ██ ██       ██      ██      
███████ ██████  ███████ ██      █████   ███████ ██   ███ █████   ███████ 
██   ██ ██      ██   ██ ██      ██  ██  ██   ██ ██    ██ ██           ██ 
██   ██ ██      ██   ██  ██████ ██   ██ ██   ██  ██████  ███████ ███████ 
[/bold rgb(0,255,255)]
"""

# Lista de pacotes necessários
REQUIRED_PACKAGES = ["requests", "rich"]

def install_packages():
    """Verifica e instala os pacotes necessários."""
    console.print(Panel.fit(INSTALL_PACKAGES_ASCII, title="Install Packages", box=ROUNDED))
    console.print("[bold cyan]🔍 Verificando pacotes necessários...[/bold cyan]")
    
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
            console.print(f"[green]✓ {package} já está instalado.[/green]")
        except ImportError:
            console.print(f"[yellow]⚠ {package} não encontrado. Instalando...[/yellow]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            console.print(f"[green]✓ {package} instalado com sucesso![/green]")
    
    console.print("\n[bold green]✅ Todos os pacotes estão prontos![/bold green]")
    console.print(Panel.fit("[bold]Pressione [Enter] para continuar...[/bold]", box=ROUNDED))
    input()

# Verifica e instala os pacotes antes de iniciar o programa
install_packages()

# Resto do seu código (o original)
import requests
from datetime import datetime
from rich.prompt import Prompt
from rich.table import Table

# Configurações
LOG_FILE = "upload_log.txt"

# Arte ASCII menor para "AUploader"
AUPLOADER_ASCII = """
[bold rgb(0,255,255)]
 █████  ██    ██ ██████  ██       ██████   █████  ██████  ███████ ██████  
██   ██ ██    ██ ██   ██ ██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
███████ ██    ██ ██████  ██      ██    ██ ███████ ██   ██ █████   ██████  
██   ██ ██    ██ ██      ██      ██    ██ ██   ██ ██   ██ ██      ██   ██ 
██   ██  ██████  ██      ███████  ██████  ██   ██ ██████  ███████ ██   ██ 
[/bold rgb(0,255,255)]
"""

# Mensagem "By Alex Lseything"
BY_MESSAGE = "[bold rgb(255,255,0)]Test Release By Alex Lseything[/bold rgb(255,255,0)]"

def upload_file(file_path):
    """Faz o upload do arquivo para o GoFile."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")
        
        url = "https://store1.gofile.io/uploadFile"
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        
        if response.status_code == 200:
            download_link = response.json()["data"]["downloadPage"]
            console.print(Panel.fit(
                f"[green]✓ Upload complete! Download link:[/green]\n[blue]{download_link}[/blue]",
                title="Success", box=ROUNDED
            ))
            
            log_entry = f"{datetime.now()} - File: {file_path} - Link: {download_link}\n"
            with open(LOG_FILE, "a") as log:
                log.write(log_entry)
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        console.print(Panel.fit(
            f"[red]✗ An error occurred during upload: {e}[/red]",
            title="Error", box=ROUNDED
        ))
    Prompt.ask("\nPress [Enter] to return to the menu")

def show_logs():
    """Exibe o histórico de uploads."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as log:
            logs = log.readlines()
            if logs:
                table = Table(title="📄 Upload History", show_header=True, header_style="bold magenta", box=ROUNDED)
                table.add_column("Date and Time", style="dim")
                table.add_column("File")
                table.add_column("Link")
                for entry in logs:
                    parts = entry.strip().split(" - ")
                    if len(parts) == 3:
                        table.add_row(parts[0], parts[1], parts[2])
                console.print(table)
            else:
                console.print(Panel.fit(
                    "[yellow]No records found.[/yellow]",
                    title="Warning", box=ROUNDED
                ))
    else:
        console.print(Panel.fit(
            "[yellow]No records found.[/yellow]",
            title="Warning", box=ROUNDED
        ))
    Prompt.ask("\nPress [Enter] to return to the menu")

def clear_logs():
    """Limpa o histórico de uploads."""
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        console.print(Panel.fit(
            "[green]✓ Upload history cleared successfully![/green]",
            title="Success", box=ROUNDED
        ))
    else:
        console.print(Panel.fit(
            "[yellow]No records found.[/yellow]",
            title="Warning", box=ROUNDED
        ))
    Prompt.ask("\nPress [Enter] to return to the menu")

def main_menu():
    """Exibe o menu principal."""
    while True:
        console.clear()
        console.print(AUPLOADER_ASCII, justify="center")
        console.print(BY_MESSAGE, justify="center")
        console.print("\n[bold cyan]🚀 File Upload Menu[/bold cyan]", justify="center")
        console.print("[bold]1. Upload a file[/bold]")
        console.print("[bold]2. View upload history[/bold]")
        console.print("[bold]3. Clear history[/bold]")
        console.print("[bold]4. Exit[/bold]")
        
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            file_path = Prompt.ask("📂 Enter the file path")
            if os.path.exists(file_path):
                upload_file(file_path)
            else:
                console.print(Panel.fit(
                    "[red]✗ File not found.[/red]",
                    title="Error", box=ROUNDED
                ))
                Prompt.ask("\nPress [Enter] to return to the menu")
        elif choice == "2":
            show_logs()
        elif choice == "3":
            clear_logs()
        elif choice == "4":
            console.print(Panel.fit(
                "[bold magenta]🚀 Exiting... Goodbye![/bold magenta]",
                title="AUploader", box=ROUNDED
            ))
            break

if __name__ == "__main__":
    main_menu()
