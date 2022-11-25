from reply import reply_message

# app = Flask(__name__)
#
#
# @app.route('/webhook/wa', methods=['POST'])
# def webhook():
#     incoming_msg = request.values.get('Body', '')
#
#
#
# if __name__ == "__main__":
#     app.run()

run = True
while run:
    incoming_msg = input(">>> ")
    if incoming_msg == "quit":
        run = False
    else:
        print(reply_message(incoming_msg))
