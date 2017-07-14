from django.conf.urls import patterns, url
from finpy import views

urlpatterns = patterns( "",
        url(r'^$', views.landing_page, name='landing_page'),
        url(r'^plotter/', views.plotter, name='plot'),
        url(r'^screener/', views.screener, name = "screener"),
        url(r'^login/',views.loggingIn, name = "loggingIn"),
        url(r'^pdfDownload/', views.pdfDownload, name = "pdfDownload"),
        url(r'^signup/',views.signup, name = "signup"),
        url(r'^altLogin/', views.altLogin, name = "altLogin"),
        url(r'^ajax/validate_username/', views.validate_username, name  = "validate_username"),
        url(r'^practiceAjax/', views.practiceAjax, name = "practiceAjax"),
        url(r'^loggingout/',views.loggingout, name = "loggingout"),
        url(r'^socialogin/',views.socialogin, name = "socialogin"),
        url(r'^practiceAjax/',views.practiceAjax, name = "practiceAjax"),
        url(r'chart/', views.chart, name = "chart"),
        url(r'screenerDash/', views.screenerDash, name = "screenerDash"),
        url(r'screenerCreate/', views.screenerCreate, name = "screenerCreate"),
        url(r'lowVolatility/',views.lowVolatility, name = "lowVolatility"),
        url(r'undervalued/', views.underValued, name = "undervalued"),
        url(r'mostPopular/', views.mostPopular, name = "mostPopular"),
        url(r'undervaluedGrowth/', views.undervalued_Growth, name = "undervaluedGrowth"),
        url(r'highGrowth/', views.highGrowth, name = "highGrowth"),
        url(r'siliconValley/', views.silicon_Valley, name = "siliconValley"),
        url(r'manufacturing/', views.Manufacturing, name = "manufacturing"),
        url(r'healthCare/', views.HealthCare, name = "healthCare"),
        url(r'finance/', views.Finance, name = "finance"),
        url(r'energy/', views.Energy, name = "energy"),












)
