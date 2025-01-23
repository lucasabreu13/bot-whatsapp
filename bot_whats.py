import pywhatkit as kit

try:
    # Substitua pelo número correto
    kit.sendwhatmsg("+5511992768803", "Eu te amo", 19, 19)  # Minuto sem o zero à esquerda
    print("Mensagem enviada ou agendada com sucesso!")
except Exception as e:
    print(f"Erro durante o envio: {e}")
