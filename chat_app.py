import flet as ft

def main(page):
    title = ft.Text("Basic Python Chatroom")

    def send_message_tunnel(message_tunnel):
        message_text = ft.Text(message_tunnel)
        chat.controls.append(message_text)
        page.update()
    
    page.pubsub.subscribe(send_message_tunnel)

    chat = ft.Column()

    def send_message(event):
        message_tunnel = f"{username.value}: {message.value}"
        page.pubsub.send_all(message_tunnel)
        message.value = ""
        page.update()

    message = ft.TextField(label="Enter your message", on_submit=send_message)
    send_button = ft.ElevatedButton("Send", on_click=send_message)

    def join_chat(event):
        page.pubsub.send_all(f"{username.value} has entered the chat.")
        page.dialog = start_popup
        start_popup.open = False
        page.remove(title)
        page.remove(start_button)
        page.add(chat)
        page.add(ft.Row([message, send_button]))
        page.update()
    
    username = ft.TextField(label="Enter your username", on_submit=join_chat)
    start_popup = ft.AlertDialog(title=ft.Text("Welcome!"), content=username, actions=[ft.ElevatedButton("Join", on_click=join_chat)])

    start_button = ft.ElevatedButton("Start Chatting", on_click=lambda e: page.open(start_popup))

    page.add(title)
    page.add(start_button)

ft.app(main, view=ft.WEB_BROWSER)