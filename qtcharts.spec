#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtcharts
Version  : 5.13.2
Release  : 18
URL      : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtcharts-everywhere-src-5.13.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtcharts-everywhere-src-5.13.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: qtcharts-lib = %{version}-%{release}
Requires: qtcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Widgets)

%description
---------------
Qt Charts
---------------
Qt Charts module provides a set of easy to use chart components. It uses
the Qt Graphics View Framework, therefore charts can be easily integrated
to modern user interfaces.

%package dev
Summary: dev components for the qtcharts package.
Group: Development
Requires: qtcharts-lib = %{version}-%{release}
Provides: qtcharts-devel = %{version}-%{release}
Requires: qtcharts = %{version}-%{release}

%description dev
dev components for the qtcharts package.


%package lib
Summary: lib components for the qtcharts package.
Group: Libraries
Requires: qtcharts-license = %{version}-%{release}

%description lib
lib components for the qtcharts package.


%package license
Summary: license components for the qtcharts package.
Group: Default

%description license
license components for the qtcharts package.


%prep
%setup -q -n qtcharts-everywhere-src-5.13.2
cd %{_builddir}/qtcharts-everywhere-src-5.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1572503883
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtcharts
cp %{_builddir}/qtcharts-everywhere-src-5.13.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtcharts/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/abstractbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/abstractchartlayout_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/abstractdomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/areachartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/axisanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/bar_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/baranimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/barchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/boxplotanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/boxplotchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/boxwhiskers_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/boxwhiskersanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/boxwhiskersdata_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/candlestick_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/candlestickanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/candlestickbodywicksanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/candlestickchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/candlestickdata_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/cartesianchartaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/cartesianchartlayout_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartaxiselement_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartbackground_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartbarcategoryaxisx_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartbarcategoryaxisy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartcategoryaxisx_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartcategoryaxisy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartconfig_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartdataset_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartdatetimeaxisx_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartdatetimeaxisy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartelement_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/charthelpers_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartlogvalueaxisx_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartlogvalueaxisy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartpresenter_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/charttheme_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemebluecerulean_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemeblueicy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemebluencs_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemebrownsand_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemedark_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemehighcontrast_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemelight_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthememanager_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemeqt_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartthemesystem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/charttitle_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartvalueaxisx_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/chartvalueaxisy_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/datetimeaxislabel_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativeabstractrendernode_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativeareaseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativeaxes_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativebarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativeboxplotseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativecandlestickseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativecategoryaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativechart_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativechartglobal_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativechartnode_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativelineseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativemargins_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativeopenglrendernode_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativepieseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativepolarchart_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativescatterseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativesplineseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativexypoint_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/declarativexyseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/editableaxislabel_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/glwidget_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/glxyseriesdata_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/horizontalaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/horizontalbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/horizontalpercentbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/horizontalstackedbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/legendlayout_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/legendmarkeritem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/legendscroller_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/linearrowitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/linechartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/logxlogydomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/logxlogypolardomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/logxydomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/logxypolardomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/percentbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/pieanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/piechartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/piesliceanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/pieslicedata_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/piesliceitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartaxisangular_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartaxisradial_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartcategoryaxisangular_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartcategoryaxisradial_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartdatetimeaxisangular_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartdatetimeaxisradial_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartlayout_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartlogvalueaxisangular_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartlogvalueaxisradial_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartvalueaxisangular_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polarchartvalueaxisradial_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/polardomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qabstractaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qabstractbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qabstractseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qarealegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qareaseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qbarcategoryaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qbarlegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qbarmodelmapper_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qbarset_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qboxplotlegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qboxplotmodelmapper_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qboxplotseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qboxset_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qcandlesticklegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qcandlestickmodelmapper_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qcandlestickseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qcandlestickset_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qcategoryaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qchart_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qchartglobal_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qchartview_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qdatetimeaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qhorizontalbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qhorizontalpercentbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qhorizontalstackedbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qlegend_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qlegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qlineseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qlogvalueaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qpercentbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qpielegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qpiemodelmapper_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qpieseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qpieslice_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qscatterseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qsplineseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qstackedbarseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qvalueaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qxylegendmarker_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qxymodelmapper_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/qxyseries_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/scatteranimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/scatterchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/scroller_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/splineanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/splinechartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/stackedbarchartitem_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/valueaxislabel_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/verticalaxis_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xlogydomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xlogypolardomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xyanimation_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xychart_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xydomain_p.h
/usr/include/qt5/QtCharts/5.13.2/QtCharts/private/xypolardomain_p.h
/usr/include/qt5/QtCharts/QAbstractAxis
/usr/include/qt5/QtCharts/QAbstractBarSeries
/usr/include/qt5/QtCharts/QAbstractSeries
/usr/include/qt5/QtCharts/QAreaLegendMarker
/usr/include/qt5/QtCharts/QAreaSeries
/usr/include/qt5/QtCharts/QBarCategoryAxis
/usr/include/qt5/QtCharts/QBarLegendMarker
/usr/include/qt5/QtCharts/QBarModelMapper
/usr/include/qt5/QtCharts/QBarSeries
/usr/include/qt5/QtCharts/QBarSet
/usr/include/qt5/QtCharts/QBoxPlotLegendMarker
/usr/include/qt5/QtCharts/QBoxPlotModelMapper
/usr/include/qt5/QtCharts/QBoxPlotSeries
/usr/include/qt5/QtCharts/QBoxSet
/usr/include/qt5/QtCharts/QCandlestickLegendMarker
/usr/include/qt5/QtCharts/QCandlestickModelMapper
/usr/include/qt5/QtCharts/QCandlestickSeries
/usr/include/qt5/QtCharts/QCandlestickSet
/usr/include/qt5/QtCharts/QCategoryAxis
/usr/include/qt5/QtCharts/QChart
/usr/include/qt5/QtCharts/QChartGlobal
/usr/include/qt5/QtCharts/QChartView
/usr/include/qt5/QtCharts/QDateTimeAxis
/usr/include/qt5/QtCharts/QHBarModelMapper
/usr/include/qt5/QtCharts/QHBoxPlotModelMapper
/usr/include/qt5/QtCharts/QHCandlestickModelMapper
/usr/include/qt5/QtCharts/QHPieModelMapper
/usr/include/qt5/QtCharts/QHXYModelMapper
/usr/include/qt5/QtCharts/QHorizontalBarSeries
/usr/include/qt5/QtCharts/QHorizontalPercentBarSeries
/usr/include/qt5/QtCharts/QHorizontalStackedBarSeries
/usr/include/qt5/QtCharts/QLegend
/usr/include/qt5/QtCharts/QLegendMarker
/usr/include/qt5/QtCharts/QLineSeries
/usr/include/qt5/QtCharts/QLogValueAxis
/usr/include/qt5/QtCharts/QPercentBarSeries
/usr/include/qt5/QtCharts/QPieLegendMarker
/usr/include/qt5/QtCharts/QPieModelMapper
/usr/include/qt5/QtCharts/QPieSeries
/usr/include/qt5/QtCharts/QPieSlice
/usr/include/qt5/QtCharts/QPolarChart
/usr/include/qt5/QtCharts/QScatterSeries
/usr/include/qt5/QtCharts/QSplineSeries
/usr/include/qt5/QtCharts/QStackedBarSeries
/usr/include/qt5/QtCharts/QVBarModelMapper
/usr/include/qt5/QtCharts/QVBoxPlotModelMapper
/usr/include/qt5/QtCharts/QVCandlestickModelMapper
/usr/include/qt5/QtCharts/QVPieModelMapper
/usr/include/qt5/QtCharts/QVXYModelMapper
/usr/include/qt5/QtCharts/QValueAxis
/usr/include/qt5/QtCharts/QXYLegendMarker
/usr/include/qt5/QtCharts/QXYModelMapper
/usr/include/qt5/QtCharts/QXYSeries
/usr/include/qt5/QtCharts/QtCharts
/usr/include/qt5/QtCharts/QtChartsDepends
/usr/include/qt5/QtCharts/QtChartsVersion
/usr/include/qt5/QtCharts/chartsnamespace.h
/usr/include/qt5/QtCharts/qabstractaxis.h
/usr/include/qt5/QtCharts/qabstractbarseries.h
/usr/include/qt5/QtCharts/qabstractseries.h
/usr/include/qt5/QtCharts/qarealegendmarker.h
/usr/include/qt5/QtCharts/qareaseries.h
/usr/include/qt5/QtCharts/qbarcategoryaxis.h
/usr/include/qt5/QtCharts/qbarlegendmarker.h
/usr/include/qt5/QtCharts/qbarmodelmapper.h
/usr/include/qt5/QtCharts/qbarseries.h
/usr/include/qt5/QtCharts/qbarset.h
/usr/include/qt5/QtCharts/qboxplotlegendmarker.h
/usr/include/qt5/QtCharts/qboxplotmodelmapper.h
/usr/include/qt5/QtCharts/qboxplotseries.h
/usr/include/qt5/QtCharts/qboxset.h
/usr/include/qt5/QtCharts/qcandlesticklegendmarker.h
/usr/include/qt5/QtCharts/qcandlestickmodelmapper.h
/usr/include/qt5/QtCharts/qcandlestickseries.h
/usr/include/qt5/QtCharts/qcandlestickset.h
/usr/include/qt5/QtCharts/qcategoryaxis.h
/usr/include/qt5/QtCharts/qchart.h
/usr/include/qt5/QtCharts/qchartglobal.h
/usr/include/qt5/QtCharts/qchartview.h
/usr/include/qt5/QtCharts/qdatetimeaxis.h
/usr/include/qt5/QtCharts/qhbarmodelmapper.h
/usr/include/qt5/QtCharts/qhboxplotmodelmapper.h
/usr/include/qt5/QtCharts/qhcandlestickmodelmapper.h
/usr/include/qt5/QtCharts/qhorizontalbarseries.h
/usr/include/qt5/QtCharts/qhorizontalpercentbarseries.h
/usr/include/qt5/QtCharts/qhorizontalstackedbarseries.h
/usr/include/qt5/QtCharts/qhpiemodelmapper.h
/usr/include/qt5/QtCharts/qhxymodelmapper.h
/usr/include/qt5/QtCharts/qlegend.h
/usr/include/qt5/QtCharts/qlegendmarker.h
/usr/include/qt5/QtCharts/qlineseries.h
/usr/include/qt5/QtCharts/qlogvalueaxis.h
/usr/include/qt5/QtCharts/qpercentbarseries.h
/usr/include/qt5/QtCharts/qpielegendmarker.h
/usr/include/qt5/QtCharts/qpiemodelmapper.h
/usr/include/qt5/QtCharts/qpieseries.h
/usr/include/qt5/QtCharts/qpieslice.h
/usr/include/qt5/QtCharts/qpolarchart.h
/usr/include/qt5/QtCharts/qscatterseries.h
/usr/include/qt5/QtCharts/qsplineseries.h
/usr/include/qt5/QtCharts/qstackedbarseries.h
/usr/include/qt5/QtCharts/qtchartsversion.h
/usr/include/qt5/QtCharts/qvalueaxis.h
/usr/include/qt5/QtCharts/qvbarmodelmapper.h
/usr/include/qt5/QtCharts/qvboxplotmodelmapper.h
/usr/include/qt5/QtCharts/qvcandlestickmodelmapper.h
/usr/include/qt5/QtCharts/qvpiemodelmapper.h
/usr/include/qt5/QtCharts/qvxymodelmapper.h
/usr/include/qt5/QtCharts/qxylegendmarker.h
/usr/include/qt5/QtCharts/qxymodelmapper.h
/usr/include/qt5/QtCharts/qxyseries.h
/usr/lib64/cmake/Qt5Charts/Qt5ChartsConfig.cmake
/usr/lib64/cmake/Qt5Charts/Qt5ChartsConfigVersion.cmake
/usr/lib64/libQt5Charts.prl
/usr/lib64/libQt5Charts.so
/usr/lib64/pkgconfig/Qt5Charts.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_charts.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_charts_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Charts.so.5
/usr/lib64/libQt5Charts.so.5.13
/usr/lib64/libQt5Charts.so.5.13.2
/usr/lib64/qt5/qml/QtCharts/designer/ChartViewSpecifics.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/AreaSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/BarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/BoxPlotSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/HorizontalBarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/HorizontalPercentBarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/HorizontalStackedBarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/LineSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PercentBarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PieSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PolarAreaSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PolarLineSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PolarScatterSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/PolarSplineSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/ScatterSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/SplineSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/default/StackedBarSeries.qml
/usr/lib64/qt5/qml/QtCharts/designer/images/areaseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/areaseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/areaseries-polar-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/areaseries-polar-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/barseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/barseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/boxplotseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/boxplotseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalbarseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalbarseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalpercentbarseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalpercentbarseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalstackedbarseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/horizontalstackedbarseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/lineseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/lineseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/lineseries-polar-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/lineseries-polar-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/percentbarseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/percentbarseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/pieseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/pieseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/scatterseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/scatterseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/scatterseries-polar-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/scatterseries-polar-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/splineseries-chart-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/splineseries-chart-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/splineseries-polar-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/splineseries-polar-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/images/stackedbarseries-icon.png
/usr/lib64/qt5/qml/QtCharts/designer/images/stackedbarseries-icon16.png
/usr/lib64/qt5/qml/QtCharts/designer/qtcharts.metainfo
/usr/lib64/qt5/qml/QtCharts/libqtchartsqml2.so
/usr/lib64/qt5/qml/QtCharts/plugins.qmltypes
/usr/lib64/qt5/qml/QtCharts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtcharts/8624bcdae55baeef00cd11d5dfcfa60f68710a02
