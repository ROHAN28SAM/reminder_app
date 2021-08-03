import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title= "Take a Break! You are doing great Job",
            message="Work is important but break is even important while working.",
            app_icon='d:\Git\Reminder Notification in Windows\icon.ico',
            timeout = 10
            )
        time.sleep(60*60*30)
        
        
    