from yookassa import Configuration, Payment
import qrcode

Configuration.account_id = 262584
Configuration.secret_key = "test_7iWPAeQpK-YPLmYtA_lfTcTHeR57sHHOoelAMPPt1w4"

payment = Payment.create({
    "amount": {
        "value": "1.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "redirect",
        "return_url": "https://www.example.com/return_url"
    },
    "capture": True,
    "description": "Заказ №37",
    "metadata": {
      "order_id": "37"
    }
})
payUrl=payment.confirmation.confirmation_url
print(payUrl)

data = payUrl
# имя конечного файла
filename = "site.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)




