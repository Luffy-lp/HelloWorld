#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HelloWorld.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    # from booktest.models import BookInfo
    # from booktest.models import HeroInfo
    # from datetime import date
    # c = BookInfo()
    # c.btitle = '倚天屠龙记'
    # c.bpub_date=date(1995,3,2)
    # c.save()
    # b = BookInfo()
    # b.btitle = '天龙八部'
    # b.bpub_date=date(1990,1,1)
    # b.save()
    # h = HeroInfo()
    # h.hname = '段誉'
    # h.hgender=False
    # h.hcomment='六脉神剑'
    # h.hbook=b
    # h.save()
    # h1 = HeroInfo()
    # h1.hname = '乔峰'
    # h1.hgender=False
    # h1.hcomment='降龙十八掌'
    # h1.hbook=b
    # h1.save()