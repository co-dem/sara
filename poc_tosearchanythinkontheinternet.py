import webbrowser as wb
var = input('введите запрос: ')

wb.open('https://www.google.by/search?q={0}&source=hp&ei=za3IYZWkB4r0U7esktAO&iflsig=ALs-wAMAAAAAYci73Y6jwM7h_ylx6AS4RpTLRPNRjXdX&ved=0ahUKEwjVvvzvhYL1AhUK-hQKHTeWBOoQ4dUDCAY&uact=5&oq=food&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDILCC4QgAQQxwEQrwEyCwguEIAEEMcBEK8BMgUIABCABDIFCAAQgAQyCwguEIAEEMcBEK8BMgUIABCABDILCC4QgAQQxwEQrwEyBQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6CAguELEDEIMBOgUILhCABDoICC4QgAQQsQM6CwguEIAEEMcBENEDOgsIABCABBCxAxCDAToOCC4QgAQQsQMQxwEQowJQAFilBGCwBWgAcAB4AIABaogB6AKSAQMzLjGYAQCgAQE&sclient=gws-wiz'.format(var))