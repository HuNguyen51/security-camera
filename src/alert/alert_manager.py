# Gửi cảnh báo
class AlertTypes:
    WARNING = 0
    INFO = 1

class AlertManager:
    def __init__(self):
        self.types = ["WARNING", "INFO"]
    def send_alert(self, alert_type, alert_message):
        # Gửi cảnh báo với thống tin alert_type và alert_message
        print(f"Sending alert: {self.types[alert_type]} - {alert_message}")