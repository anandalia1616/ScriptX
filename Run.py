from Penyimpanan.FolderSC.facebook import Facebook
from rich.panel import Panel
from rich.console import Console
from Temporary.Terminalize.Styles import style_terminal

class Main:
    def __init__(self) -> None:
        pass
        
    def BruteForce(self):
        try:
            created = '24 Oktober 2024'
            expired = 'unlimited'
            sisa = 'unlimited'
            Facebook().Chek_Cookies(created,expired,sisa)
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
            
Main().BruteForce()
        