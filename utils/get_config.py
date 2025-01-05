import paramiko
from scp import SCPClient

def get_config(name):
    host = "178.208.80.140"
    username = "root"
    remote_path = f"/root/{name}.sswan"
    local_path = "./utils/save_vpn_config"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username,password="QtA3K9fbXJ")

        with SCPClient(ssh.get_transport()) as scp:
            scp.get(remote_path, local_path)
        return "Файл успешно загружен!"
    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        ssh.close()
