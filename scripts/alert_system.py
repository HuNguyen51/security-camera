# Kích hoạt cảnh báo khi có đối tượng lạ
from src.alert.alert_manager import AlertManager
from src.alert.roi_checker import RoiChecker

am = AlertManager()
rc = RoiChecker()

def roi_check(frame, point, draw=False):
    return  rc.is_inside_forbidden_zone(frame, point, draw)

def alert(alert_types, alert_messages):
    am.send_alert(alert_types, alert_messages)