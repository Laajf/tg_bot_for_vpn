from utils.create_config import create_config
from utils.get_config import get_config
from utils.get_name import get_name

def create_and_get_config(month):
    try:
        print(1)
        name = get_name()
        print(2)
        create_config(name, month)
        print(3)
        get_config(name)
        print(4)
        return f"utils/save_vpn_config/{name}"

    except Exception as e:
        return str(e)
