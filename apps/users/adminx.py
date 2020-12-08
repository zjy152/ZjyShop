import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = '生鲜超市后台管理系统'
    site_footer = "Powered By 1906c - 2020"
    menu_style = 'accordion'            # 菜单收缩


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']




xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)