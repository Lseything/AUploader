import os
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.box import ROUNDED
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress
import requests
from datetime import datetime

# Configurações
console = Console()

# Arte ASCII para "Install Packages"
INSTALL_PACKAGES_ASCII = """
[bold rgb(0,255,255)]
 ▄▄▄      ██▓███  ▄▄▄      ▄████▄  ██ ▄█▄▄▄       ▄████▓█████  ██████ 
▒████▄   ▓██░  ██▒████▄   ▒██▀ ▀█  ██▄█▒████▄    ██▒ ▀█▓█   ▀▒██    ▒ 
▒██  ▀█▄ ▓██░ ██▓▒██  ▀█▄ ▒▓█    ▄▓███▄▒██  ▀█▄ ▒██░▄▄▄▒███  ░ ▓██▄   
░██▄▄▄▄██▒██▄█▓▒ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █░██▄▄▄▄██░▓█  ██▒▓█  ▄  ▒   ██▒
 ▓█   ▓██▒██▒ ░  ░▓█   ▓██▒ ▓███▀ ▒██▒ █▓█   ▓██░▒▓███▀░▒████▒██████▒▒
 ▒▒   ▓▒█▒▓▒░ ░  ░▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒▒   ▓▒█░░▒   ▒░░ ▒░ ▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░▒ ░      ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░▒   ▒▒ ░ ░   ░ ░ ░  ░ ░▒  ░ ░
  ░   ▒  ░░        ░   ▒  ░       ░ ░░ ░ ░   ▒  ░ ░   ░   ░  ░  ░  ░  
      ░  ░             ░  ░ ░     ░  ░       ░  ░     ░   ░  ░     ░  
[/bold rgb(0,255,255)]
"""

# Lista de pacotes necessários
REQUIRED_PACKAGES = ["requests", "rich", "datetime"]

def install_packages():
    """Verifica e instala os pacotes necessários."""
    console.print(Panel.fit(INSTALL_PACKAGES_ASCII, title="Install Packages", box=ROUNDED))
    console.print("[bold cyan]🔍 Checking required packages...[/bold cyan]")
    
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
            console.print(f"[green]✓ {package} is already installed.[/green]")
        except ImportError:
            console.print(f"[yellow]⚠ {package} not found. Installing...[/yellow]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            console.print(f"[green]✓ {package} installed successfully![/green]")
    
    console.print("\n[bold green]✅ All packages are ready![/bold green]")
    console.print(Panel.fit("[bold]Press [Enter] to continue...[/bold]", box=ROUNDED))
    input()

# Verifica e instala os pacotes antes de iniciar o programa
install_packages()

# Resto do seu código (o original)
LOG_FILE = "upload_log.txt"

# Arte ASCII menor para "AUploader"
AUPLOADER_ASCII = """
[bold rgb(0,255,255)]
 ▄▄▄      █    ██ ██▓███  ██▓    ▒█████  ▄▄▄     ▓█████▄▓█████ ██▀███  
▒████▄    ██  ▓██▓██░  ██▓██▒   ▒██▒  ██▒████▄   ▒██▀ ██▓█   ▀▓██ ▒ ██▒
▒██  ▀█▄ ▓██  ▒██▓██░ ██▓▒██░   ▒██░  ██▒██  ▀█▄ ░██   █▒███  ▓██ ░▄█ ▒
░██▄▄▄▄██▓▓█  ░██▒██▄█▓▒ ▒██░   ▒██   ██░██▄▄▄▄██░▓█▄   ▒▓█  ▄▒██▀▀█▄  
 ▓█   ▓██▒▒█████▓▒██▒ ░  ░██████░ ████▓▒░▓█   ▓██░▒████▓░▒████░██▓ ▒██▒
 ▒▒   ▓▒█░▒▓▒ ▒ ▒▒▓▒░ ░  ░ ▒░▓  ░ ▒░▒░▒░ ▒▒   ▓▒█░▒▒▓  ▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░▒░ ░ ░░▒ ░    ░ ░ ▒  ░ ░ ▒ ▒░  ▒   ▒▒ ░░ ▒  ▒ ░ ░  ░ ░▒ ░ ▒░
  ░   ▒   ░░░ ░ ░░░        ░ ░  ░ ░ ░ ▒   ░   ▒   ░ ░  ░   ░    ░░   ░ 
      ░  ░  ░                ░  ░   ░ ░       ░  ░  ░      ░  ░  ░     
[/bold rgb(0,255,255)]
"""

# Mensagem "By Alex Lseything"
BY_MESSAGE = "[bold rgb(255,255,0)]Test Release By Alex Lseything[/bold rgb(255,255,0)]"

# Dicionário de idiomas
LANGUAGES = {
    "English": {
        "welcome": "Welcome to AUploader!",
        "upload_success": "✓ Upload complete! Download link:",
        "file_not_found": "✗ File not found.",
        "upload_error": "✗ An error occurred during upload:",
        "history_title": "📄 Upload History",
        "no_records": "No records found.",
        "history_cleared": "✓ Upload history cleared successfully!",
        "menu_title": "🚀 File Upload Menu",
        "menu_options": ["Upload a file", "View upload history", "Clear history", "Exit"],
        "enter_file_path": "📂 Enter the file path",
        "choose_service": "🌐 Choose the upload service (1: GoFile, 2: BashUpload, 3: File.io)",
        "press_enter": "Press [Enter] to return to the menu",
        "exiting": "🚀 Exiting... Goodbye!",
    },
    "Portuguese": {
        "welcome": "Bem-vindo ao AUploader!",
        "upload_success": "✓ Upload concluído! Link de download:",
        "file_not_found": "✗ Arquivo não encontrado.",
        "upload_error": "✗ Ocorreu um erro durante o upload:",
        "history_title": "📄 Histórico de Uploads",
        "no_records": "Nenhum registro encontrado.",
        "history_cleared": "✓ Histórico de uploads limpo com sucesso!",
        "menu_title": "🚀 Menu de Upload de Arquivos",
        "menu_options": ["Fazer upload de um arquivo", "Ver histórico de uploads", "Limpar histórico", "Sair"],
        "enter_file_path": "📂 Digite o caminho do arquivo",
        "choose_service": "🌐 Escolha o serviço de upload (1: GoFile, 2: BashUpload, 3: File.io)",
        "press_enter": "Pressione [Enter] para voltar ao menu",
        "exiting": "🚀 Saindo... Adeus!",
    },
    "Spanish": {
        "welcome": "¡Bienvenido a AUploader!",
        "upload_success": "✓ ¡Subida completada! Enlace de descarga:",
        "file_not_found": "✗ Archivo no encontrado.",
        "upload_error": "✗ Ocurrió un error durante la subida:",
        "history_title": "📄 Historial de Subidas",
        "no_records": "No se encontraron registros.",
        "history_cleared": "✓ ¡Historial de subidas borrado con éxito!",
        "menu_title": "🚀 Menú de Subida de Archivos",
        "menu_options": ["Subir un archivo", "Ver historial de subidas", "Borrar historial", "Salir"],
        "enter_file_path": "📂 Ingrese la ruta del archivo",
        "choose_service": "🌐 Elija el servicio de subida (1: GoFile, 2: BashUpload, 3: File.io)",
        "press_enter": "Presione [Enter] para volver al menú",
        "exiting": "🚀 Saliendo... ¡Adiós!",
    },
    "Russian": {
        "welcome": "Добро пожаловать в AUploader!",
        "upload_success": "✓ Загрузка завершена! Ссылка для скачивания:",
        "file_not_found": "✗ Файл не найден.",
        "upload_error": "✗ Произошла ошибка во время загрузки:",
        "history_title": "📄 История Загрузок",
        "no_records": "Записи не найдены.",
        "history_cleared": "✓ История загрузок успешно очищена!",
        "menu_title": "🚀 Меню Загрузки Файлов",
        "menu_options": ["Загрузить файл", "Просмотреть историю загрузок", "Очистить историю", "Выход"],
        "enter_file_path": "📂 Введите путь к файлу",
        "choose_service": "🌐 Выберите сервис загрузки (1: GoFile, 2: BashUpload, 3: File.io)",
        "press_enter": "Нажмите [Enter], чтобы вернуться в меню",
        "exiting": "🚀 Выход... До свидания!",
    },
    "Ukrainian": {
        "welcome": "Ласкаво просимо до AUploader!",
        "upload_success": "✓ Завантаження завершено! Посилання для завантаження:",
        "file_not_found": "✗ Файл не знайдено.",
        "upload_error": "✗ Під час завантаження сталася помилка:",
        "history_title": "📄 Історія Завантажень",
        "no_records": "Записи не знайдено.",
        "history_cleared": "✓ Історію завантажень успішно очищено!",
        "menu_title": "🚀 Меню Завантаження Файлів",
        "menu_options": ["Завантажити файл", "Переглянути історію завантажень", "Очистити історію", "Вийти"],
        "enter_file_path": "📂 Введіть шлях до файлу",
        "choose_service": "🌐 Виберіть сервіс завантаження (1: GoFile, 2: BashUpload, 3: File.io)",
        "press_enter": "Натисніть [Enter], щоб повернутися до меню",
        "exiting": "🚀 Виходжу... До побачення!",
    },
}

class FileUploader:
    """Classe para gerenciar o upload de arquivos."""

    def __init__(self, language):
        self.language = language

    def upload_to_gofile(self, file_path):
        """Faz o upload do arquivo para o GoFile."""
        url = "https://store1.gofile.io/uploadFile"
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            return response.json()["data"]["downloadPage"]  # Retorna o link de download
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def upload_to_bashupload(self, file_path):
        """Faz o upload do arquivo para o BashUpload."""
        url = "https://bashupload.com/"
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            # Retorna a mensagem original do BashUpload
            return response.text.strip()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def upload_to_fileio(self, file_path):
        """Faz o upload do arquivo para o File.io."""
        url = "https://file.io/"
        with open(file_path, "rb") as file:
            response = requests.post(url, files={"file": file})
        if response.status_code == 200:
            return response.json()["link"]  # Retorna o link de download
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

    def upload_file(self, file_path, service):
        """Faz o upload do arquivo para o serviço selecionado."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(LANGUAGES[self.language]["file_not_found"])
            
            if service == "1":
                download_link = self.upload_to_gofile(file_path)
                console.print(Panel.fit(
                    f"[green]{LANGUAGES[self.language]['upload_success']}[/green]\n[blue]{download_link}[/blue]",
                    title="Success", box=ROUNDED
                ))
            elif service == "2":
                bashupload_message = self.upload_to_bashupload(file_path)
                console.print(Panel.fit(
                    f"[green]{bashupload_message}[/green]",
                    title="Success", box=ROUNDED
                ))
            elif service == "3":
                download_link = self.upload_to_fileio(file_path)
                console.print(Panel.fit(
                    f"[green]{LANGUAGES[self.language]['upload_success']}[/green]\n[blue]{download_link}[/blue]",
                    title="Success", box=ROUNDED
                ))
            else:
                raise ValueError("Invalid service selected.")
            
            log_entry = f"{datetime.now()} - File: {file_path} - Link: {download_link if service in ['1', '3'] else bashupload_message}\n"
            with open(LOG_FILE, "a") as log:
                log.write(log_entry)
        except Exception as e:
            console.print(Panel.fit(
                f"[red]{LANGUAGES[self.language]['upload_error']} {e}[/red]",
                title="Error", box=ROUNDED
            ))
        Prompt.ask(f"\n{LANGUAGES[self.language]['press_enter']}")

    def show_logs(self):
        """Exibe o histórico de uploads."""
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as log:
                logs = log.readlines()
                if logs:
                    table = Table(title=LANGUAGES[self.language]["history_title"], show_header=True, header_style="bold magenta", box=ROUNDED)
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
                        f"[yellow]{LANGUAGES[self.language]['no_records']}[/yellow]",
                        title="Warning", box=ROUNDED
                    ))
        else:
            console.print(Panel.fit(
                f"[yellow]{LANGUAGES[self.language]['no_records']}[/yellow]",
                title="Warning", box=ROUNDED
            ))
        Prompt.ask(f"\n{LANGUAGES[self.language]['press_enter']}")

    def clear_logs(self):
        """Limpa o histórico de uploads."""
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
            console.print(Panel.fit(
                f"[green]{LANGUAGES[self.language]['history_cleared']}[/green]",
                title="Success", box=ROUNDED
            ))
        else:
            console.print(Panel.fit(
                f"[yellow]{LANGUAGES[self.language]['no_records']}[/yellow]",
                title="Warning", box=ROUNDED
            ))
        Prompt.ask(f"\n{LANGUAGES[self.language]['press_enter']}")

def select_language():
    """Permite ao usuário selecionar o idioma."""
    console.clear()
    console.print(Panel.fit("[bold]🌍 Select your language[/bold]", box=ROUNDED))
    console.print("[bold]1. English[/bold]")
    console.print("[bold]2. Portuguese[/bold]")
    console.print("[bold]3. Spanish[/bold]")
    console.print("[bold]4. Russian[/bold]")
    console.print("[bold]5. Ukrainian[/bold]")
    
    choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])
    
    # Define o idioma com base na escolha do usuário
    if choice == "1":
        return "English"
    elif choice == "2":
        return "Portuguese"
    elif choice == "3":
        return "Spanish"
    elif choice == "4":
        return "Russian"
    elif choice == "5":
        return "Ukrainian"

def main_menu():
    """Exibe o menu principal."""
    language = select_language()
    uploader = FileUploader(language)
    
    while True:
        console.clear()
        console.print(AUPLOADER_ASCII, justify="center")
        console.print(BY_MESSAGE, justify="center")
        console.print(f"\n[bold cyan]{LANGUAGES[language]['menu_title']}[/bold cyan]", justify="center")
        for i, option in enumerate(LANGUAGES[language]["menu_options"], start=1):
            console.print(f"[bold]{i}. {option}[/bold]")
        
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"])

        if choice == "1":
            file_path = Prompt.ask(LANGUAGES[language]["enter_file_path"])
            if os.path.exists(file_path):
                service = Prompt.ask(LANGUAGES[language]["choose_service"], choices=["1", "2", "3"])
                uploader.upload_file(file_path, service)
            else:
                console.print(Panel.fit(
                    f"[red]{LANGUAGES[language]['file_not_found']}[/red]",
                    title="Error", box=ROUNDED
                ))
                Prompt.ask(f"\n{LANGUAGES[language]['press_enter']}")
        elif choice == "2":
            uploader.show_logs()
        elif choice == "3":
            uploader.clear_logs()
        elif choice == "4":
            console.print(Panel.fit(
                f"[bold magenta]{LANGUAGES[language]['exiting']}[/bold magenta]",
                title="AUploader", box=ROUNDED
            ))
            break

if __name__ == "__main__":
    main_menu()
