from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        logging.info(f"Получены данные: {data}")

        # Проверяем статус платежа
        if data.get('status') == 'success':
            order_id = data.get('order_id')
            amount_received = data.get('received_amount')
            currency = data.get('pay_currency')
            logging.info(f"Платеж успешно завершен для заказа {order_id}. Получено {amount_received} {currency}")
        else:
            logging.error("Платеж не был успешен.")

        # Возвращаем ответ, подтверждающий получение данных
        return jsonify({"status": "received"}), 200

    except Exception as e:
        # Логируем ошибку, если что-то пошло не так
        logging.error(f"Ошибка при обработке данных: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400


if __name__ == '__main__':
    # Запускаем сервер
    app.run(host='0.0.0.0', port=5000)
