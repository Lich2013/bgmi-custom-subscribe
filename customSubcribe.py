#!/usr/bin/env python3
#coding:utf-8

import os
import time
import argparse
from bgmi.lib.models import STATUS_UPDATED, STATUS_UPDATING, STATUS_FOLLOWED, Bangumi, Followed, Filter
from bgmi.lib.controllers import filter_
from config import SUBCRIBE_BANGUMI


def customSubcribeBangumi():
    for name in SUBCRIBE_BANGUMI:  
        episode = SUBCRIBE_BANGUMI[name]['episode'] if 'episode' in SUBCRIBE_BANGUMI[name] else 0
        keyword = SUBCRIBE_BANGUMI[name].get('keyword', None)
        cover = SUBCRIBE_BANGUMI[name].get('cover', None)
        if keyword is None or cover is None:
            result = {
            "status": "error",
            "message": f"{name} keyword/cover not found, please check the keyword/cover",
            }
            return result
        bangumi, isCreated = Bangumi.get_or_create(
                name=name, defaults={"status": STATUS_UPDATING, "keyword":keyword, 'update_time':'Unknown', 'cover':cover}
            )

        if not isCreated:
            if SUBCRIBE_BANGUMI[name]['isUpdating']:
                bangumi.status = STATUS_UPDATING
                bangumi.save()
                print(name, " subcribed and updated")
            else:
                print(name, " subcribed")
        follow, isfollowed = Followed.get_or_create(
                bangumi_name=name, defaults={"status": STATUS_FOLLOWED, "episode": 0}
            )
        if not isfollowed:
            if SUBCRIBE_BANGUMI[name]['isUpdating']:
                t = int(time.time())
                follow.updated_time = t
                follow.save()
                print(name, " update update_time ", t)

            print(name, " followed")
        Filter.get_or_create(bangumi_name=name)
        filter_(name)

def installCron():
    """
    install crontab
    """
    script_path = os.path.realpath(__file__)
    cmd = '(crontab -l ; echo "0 */2 * * * ' \
          'LC_ALL=en_US.UTF-8 python3 ' + script_path + ' run") | crontab -'
    os.system(cmd)
    print("install success")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BGmi custom subcribe tool')
    parser.add_argument(dest='action', metavar='action',
                        help='run、install_cron')
    args = parser.parse_args()
    action = args.action
    if action == 'run':
        print(customSubcribeBangumi())
    elif action == 'install_cron':
        installCron()
    else:
        print("action error")
        exit(1)
