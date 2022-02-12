print(33)

try:
    from notify import send
except:
    logger.info("无推送文件")

try:
    send('WSKEY转换', 'te_xt')
except:
    logger.info("通知发送失败")