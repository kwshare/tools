#!/usr/bin/python
# coding:utf-8

# main function

import send_cmd
import config

while 1:
    print '---------vultr simple python client---------------'
    print '1. account/info'
    print '2. auth/info'
    print '3. server/bandwidth'
    print '4. server/halt'
    print '5. server/list'
    print '6. server/reboot'
    print '7. server/start'
    print '8. snapshot/create'

    select = raw_input('>')
    if not select.isdigit():
        print 'Bye.'
        break

    elif select == '1':
        send_cmd.get('account/info', True)
    elif select == '2':
        send_cmd.get('auth/info', True)
    elif select == '3':
        send_cmd.get('server/bandwidth', True, config.SERVER_ID)
    elif select == '4':
        if raw_input('Are you sure about this?(y/N)') == 'y':
            send_cmd.post('server/halt', True, config.SERVER_ID)
    elif select == '5':
        if raw_input('Are you sure about this?(y/N)') == 'y':
            send_cmd.post('server/list', True, config.SERVER_ID)
    elif select == '6':
        if raw_input('Are you sure about this?(y/N)') == 'y':
            send_cmd.post('server/reboot', True, config.SERVER_ID)
    elif select == '7':
        if raw_input('Are you sure about this?(y/N)') == 'y':
            send_cmd.post('server/start', True, config.SERVER_ID)
    elif select == '8':
        send_cmd.post('snapshot/create', True, config.SERVER_ID)
    else:
        print 'Wrong choice'
