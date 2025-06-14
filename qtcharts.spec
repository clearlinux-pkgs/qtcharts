#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: qmake5
# autospec version: v27
# autospec commit: 65cf152
#
Name     : qtcharts
Version  : 5.15.17
Release  : 30
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.17/submodules/qtcharts-everywhere-opensource-src-5.15.17.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.17/submodules/qtcharts-everywhere-opensource-src-5.15.17.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: qtcharts-lib = %{version}-%{release}
Requires: qtcharts-license = %{version}-%{release}
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Widgets)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package examples
Summary: examples components for the qtcharts package.
Group: Default
Requires: qtcharts-dev = %{version}-%{release}

%description examples
examples components for the qtcharts package.


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
%setup -q -n qtcharts-everywhere-src-5.15.17
cd %{_builddir}/qtcharts-everywhere-src-5.15.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export QMAKE_CFLAGS="$CFLAGS"
export QMAKE_CXXFLAGS="$CXXFLAGS"
export QMAKE_LFLAGS="$LDFLAGS"
export QMAKE_LIBDIR=/usr/lib64
export QMAKE_CFLAGS_RELEASE=
export QMAKE_CXXFLAGS_RELEASE=
export PATH=/usr/lib64/qt5/bin:$PATH
qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1748635067
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtcharts
cp %{_builddir}/qtcharts-everywhere-src-%{version}/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtcharts/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/abstractbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/abstractchartlayout_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/abstractdomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/areachartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/axisanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/bar_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/baranimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/barchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/boxplotanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/boxplotchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/boxwhiskers_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/boxwhiskersanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/boxwhiskersdata_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/candlestick_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/candlestickanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/candlestickbodywicksanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/candlestickchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/candlestickdata_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/cartesianchartaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/cartesianchartlayout_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartaxiselement_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartbackground_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartbarcategoryaxisx_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartbarcategoryaxisy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartcategoryaxisx_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartcategoryaxisy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartconfig_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartdataset_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartdatetimeaxisx_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartdatetimeaxisy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartelement_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/charthelpers_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartlogvalueaxisx_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartlogvalueaxisy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartpresenter_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/charttheme_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemebluecerulean_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemeblueicy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemebluencs_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemebrownsand_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemedark_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemehighcontrast_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemelight_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthememanager_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemeqt_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartthemesystem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/charttitle_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartvalueaxisx_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/chartvalueaxisy_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/datetimeaxislabel_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativeabstractrendernode_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativeareaseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativeaxes_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativebarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativeboxplotseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativecandlestickseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativecategoryaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativechart_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativechartglobal_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativechartnode_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativelineseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativemargins_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativeopenglrendernode_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativepieseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativepolarchart_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativescatterseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativesplineseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativexypoint_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/declarativexyseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/editableaxislabel_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/glwidget_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/glxyseriesdata_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/horizontalaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/horizontalbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/horizontalpercentbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/horizontalstackedbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/legendlayout_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/legendmarkeritem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/legendscroller_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/linearrowitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/linechartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/logxlogydomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/logxlogypolardomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/logxydomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/logxypolardomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/percentbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/pieanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/piechartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/piesliceanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/pieslicedata_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/piesliceitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartaxisangular_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartaxisradial_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartcategoryaxisangular_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartcategoryaxisradial_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartdatetimeaxisangular_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartdatetimeaxisradial_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartlayout_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartlogvalueaxisangular_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartlogvalueaxisradial_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartvalueaxisangular_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polarchartvalueaxisradial_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/polardomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qabstractaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qabstractbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qabstractseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qarealegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qareaseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qbarcategoryaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qbarlegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qbarmodelmapper_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qbarset_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qboxplotlegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qboxplotmodelmapper_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qboxplotseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qboxset_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qcandlesticklegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qcandlestickmodelmapper_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qcandlestickseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qcandlestickset_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qcategoryaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qchart_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qchartglobal_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qchartview_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qdatetimeaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qhorizontalbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qhorizontalpercentbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qhorizontalstackedbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qlegend_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qlegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qlineseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qlogvalueaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qpercentbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qpielegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qpiemodelmapper_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qpieseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qpieslice_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qscatterseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qsplineseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qstackedbarseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qvalueaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qxylegendmarker_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qxymodelmapper_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/qxyseries_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/scatteranimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/scatterchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/scroller_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/splineanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/splinechartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/stackedbarchartitem_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/valueaxislabel_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/verticalaxis_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xlogydomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xlogypolardomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xyanimation_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xychart_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xydomain_p.h
/usr/include/qt5/QtCharts/5.15.17/QtCharts/private/xypolardomain_p.h
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

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/charts/areachart/areachart.pro
/usr/share/qt5/examples/charts/areachart/main.cpp
/usr/share/qt5/examples/charts/audio/audio.pro
/usr/share/qt5/examples/charts/audio/main.cpp
/usr/share/qt5/examples/charts/audio/widget.cpp
/usr/share/qt5/examples/charts/audio/widget.h
/usr/share/qt5/examples/charts/audio/xyseriesiodevice.cpp
/usr/share/qt5/examples/charts/audio/xyseriesiodevice.h
/usr/share/qt5/examples/charts/barchart/barchart.pro
/usr/share/qt5/examples/charts/barchart/main.cpp
/usr/share/qt5/examples/charts/barmodelmapper/barmodelmapper.pro
/usr/share/qt5/examples/charts/barmodelmapper/customtablemodel.cpp
/usr/share/qt5/examples/charts/barmodelmapper/customtablemodel.h
/usr/share/qt5/examples/charts/barmodelmapper/main.cpp
/usr/share/qt5/examples/charts/barmodelmapper/tablewidget.cpp
/usr/share/qt5/examples/charts/barmodelmapper/tablewidget.h
/usr/share/qt5/examples/charts/boxplotchart/acme_data.txt
/usr/share/qt5/examples/charts/boxplotchart/boxdatareader.cpp
/usr/share/qt5/examples/charts/boxplotchart/boxdatareader.h
/usr/share/qt5/examples/charts/boxplotchart/boxplotchart.pro
/usr/share/qt5/examples/charts/boxplotchart/boxplotdata.qrc
/usr/share/qt5/examples/charts/boxplotchart/boxwhisk_data.txt
/usr/share/qt5/examples/charts/boxplotchart/main.cpp
/usr/share/qt5/examples/charts/callout/callout.cpp
/usr/share/qt5/examples/charts/callout/callout.h
/usr/share/qt5/examples/charts/callout/callout.pro
/usr/share/qt5/examples/charts/callout/main.cpp
/usr/share/qt5/examples/charts/callout/view.cpp
/usr/share/qt5/examples/charts/callout/view.h
/usr/share/qt5/examples/charts/candlestickchart/acme_data.txt
/usr/share/qt5/examples/charts/candlestickchart/candlestickchart.pro
/usr/share/qt5/examples/charts/candlestickchart/candlestickdata.qrc
/usr/share/qt5/examples/charts/candlestickchart/candlestickdatareader.cpp
/usr/share/qt5/examples/charts/candlestickchart/candlestickdatareader.h
/usr/share/qt5/examples/charts/candlestickchart/main.cpp
/usr/share/qt5/examples/charts/chartinteractions/chart.cpp
/usr/share/qt5/examples/charts/chartinteractions/chart.h
/usr/share/qt5/examples/charts/chartinteractions/chartinteractions.pro
/usr/share/qt5/examples/charts/chartinteractions/chartview.cpp
/usr/share/qt5/examples/charts/chartinteractions/chartview.h
/usr/share/qt5/examples/charts/chartinteractions/main.cpp
/usr/share/qt5/examples/charts/charts.pro
/usr/share/qt5/examples/charts/chartthemes/chartthemes.pro
/usr/share/qt5/examples/charts/chartthemes/main.cpp
/usr/share/qt5/examples/charts/chartthemes/themewidget.cpp
/usr/share/qt5/examples/charts/chartthemes/themewidget.h
/usr/share/qt5/examples/charts/chartthemes/themewidget.ui
/usr/share/qt5/examples/charts/customchart/customchart.pro
/usr/share/qt5/examples/charts/customchart/main.cpp
/usr/share/qt5/examples/charts/datetimeaxis/datetimeaxis.pro
/usr/share/qt5/examples/charts/datetimeaxis/main.cpp
/usr/share/qt5/examples/charts/datetimeaxis/sun_spots.txt
/usr/share/qt5/examples/charts/datetimeaxis/sundata.qrc
/usr/share/qt5/examples/charts/donutbreakdown/donutbreakdown.pro
/usr/share/qt5/examples/charts/donutbreakdown/donutbreakdownchart.cpp
/usr/share/qt5/examples/charts/donutbreakdown/donutbreakdownchart.h
/usr/share/qt5/examples/charts/donutbreakdown/main.cpp
/usr/share/qt5/examples/charts/donutbreakdown/mainslice.cpp
/usr/share/qt5/examples/charts/donutbreakdown/mainslice.h
/usr/share/qt5/examples/charts/donutchart/donutchart.pro
/usr/share/qt5/examples/charts/donutchart/main.cpp
/usr/share/qt5/examples/charts/dynamicspline/chart.cpp
/usr/share/qt5/examples/charts/dynamicspline/chart.h
/usr/share/qt5/examples/charts/dynamicspline/dynamicspline.pro
/usr/share/qt5/examples/charts/dynamicspline/main.cpp
/usr/share/qt5/examples/charts/horizontalbarchart/horizontalbarchart.pro
/usr/share/qt5/examples/charts/horizontalbarchart/main.cpp
/usr/share/qt5/examples/charts/horizontalpercentbarchart/horizontalpercentbarchart.pro
/usr/share/qt5/examples/charts/horizontalpercentbarchart/main.cpp
/usr/share/qt5/examples/charts/horizontalstackedbarchart/horizontalstackedbarchart.pro
/usr/share/qt5/examples/charts/horizontalstackedbarchart/main.cpp
/usr/share/qt5/examples/charts/legend/legend.pro
/usr/share/qt5/examples/charts/legend/main.cpp
/usr/share/qt5/examples/charts/legend/mainwidget.cpp
/usr/share/qt5/examples/charts/legend/mainwidget.h
/usr/share/qt5/examples/charts/legendmarkers/legendmarkers.pro
/usr/share/qt5/examples/charts/legendmarkers/main.cpp
/usr/share/qt5/examples/charts/legendmarkers/mainwidget.cpp
/usr/share/qt5/examples/charts/legendmarkers/mainwidget.h
/usr/share/qt5/examples/charts/lineandbar/lineandbar.pro
/usr/share/qt5/examples/charts/lineandbar/main.cpp
/usr/share/qt5/examples/charts/linechart/linechart.pro
/usr/share/qt5/examples/charts/linechart/main.cpp
/usr/share/qt5/examples/charts/logvalueaxis/logvalueaxis.pro
/usr/share/qt5/examples/charts/logvalueaxis/main.cpp
/usr/share/qt5/examples/charts/modeldata/customtablemodel.cpp
/usr/share/qt5/examples/charts/modeldata/customtablemodel.h
/usr/share/qt5/examples/charts/modeldata/main.cpp
/usr/share/qt5/examples/charts/modeldata/modeldata.pro
/usr/share/qt5/examples/charts/modeldata/tablewidget.cpp
/usr/share/qt5/examples/charts/modeldata/tablewidget.h
/usr/share/qt5/examples/charts/multiaxis/main.cpp
/usr/share/qt5/examples/charts/multiaxis/multiaxis.pro
/usr/share/qt5/examples/charts/nesteddonuts/main.cpp
/usr/share/qt5/examples/charts/nesteddonuts/nesteddonuts.pro
/usr/share/qt5/examples/charts/nesteddonuts/widget.cpp
/usr/share/qt5/examples/charts/nesteddonuts/widget.h
/usr/share/qt5/examples/charts/openglseries/datasource.cpp
/usr/share/qt5/examples/charts/openglseries/datasource.h
/usr/share/qt5/examples/charts/openglseries/main.cpp
/usr/share/qt5/examples/charts/openglseries/openglseries.pro
/usr/share/qt5/examples/charts/percentbarchart/main.cpp
/usr/share/qt5/examples/charts/percentbarchart/percentbarchart.pro
/usr/share/qt5/examples/charts/piechart/main.cpp
/usr/share/qt5/examples/charts/piechart/piechart.pro
/usr/share/qt5/examples/charts/piechartcustomization/brushtool.cpp
/usr/share/qt5/examples/charts/piechartcustomization/brushtool.h
/usr/share/qt5/examples/charts/piechartcustomization/customslice.cpp
/usr/share/qt5/examples/charts/piechartcustomization/customslice.h
/usr/share/qt5/examples/charts/piechartcustomization/main.cpp
/usr/share/qt5/examples/charts/piechartcustomization/mainwidget.cpp
/usr/share/qt5/examples/charts/piechartcustomization/mainwidget.h
/usr/share/qt5/examples/charts/piechartcustomization/pentool.cpp
/usr/share/qt5/examples/charts/piechartcustomization/pentool.h
/usr/share/qt5/examples/charts/piechartcustomization/piechartcustomization.pro
/usr/share/qt5/examples/charts/piechartdrilldown/drilldownchart.cpp
/usr/share/qt5/examples/charts/piechartdrilldown/drilldownchart.h
/usr/share/qt5/examples/charts/piechartdrilldown/drilldownslice.cpp
/usr/share/qt5/examples/charts/piechartdrilldown/drilldownslice.h
/usr/share/qt5/examples/charts/piechartdrilldown/main.cpp
/usr/share/qt5/examples/charts/piechartdrilldown/piechartdrilldown.pro
/usr/share/qt5/examples/charts/polarchart/chartview.cpp
/usr/share/qt5/examples/charts/polarchart/chartview.h
/usr/share/qt5/examples/charts/polarchart/main.cpp
/usr/share/qt5/examples/charts/polarchart/polarchart.pro
/usr/share/qt5/examples/charts/qmlaxes/main.cpp
/usr/share/qt5/examples/charts/qmlaxes/qml/qmlaxes/View1.qml
/usr/share/qt5/examples/charts/qmlaxes/qml/qmlaxes/View2.qml
/usr/share/qt5/examples/charts/qmlaxes/qml/qmlaxes/View3.qml
/usr/share/qt5/examples/charts/qmlaxes/qml/qmlaxes/main.qml
/usr/share/qt5/examples/charts/qmlaxes/qmlaxes.pro
/usr/share/qt5/examples/charts/qmlaxes/resources.qrc
/usr/share/qt5/examples/charts/qmlboxplot/main.cpp
/usr/share/qt5/examples/charts/qmlboxplot/qml/qmlboxplot/main.qml
/usr/share/qt5/examples/charts/qmlboxplot/qmlboxplot.pro
/usr/share/qt5/examples/charts/qmlboxplot/resources.qrc
/usr/share/qt5/examples/charts/qmlcandlestick/main.cpp
/usr/share/qt5/examples/charts/qmlcandlestick/qml/qmlcandlestick/main.qml
/usr/share/qt5/examples/charts/qmlcandlestick/qmlcandlestick.pro
/usr/share/qt5/examples/charts/qmlcandlestick/resources.qrc
/usr/share/qt5/examples/charts/qmlchart/main.cpp
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/MainForm.ui.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View1.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View10.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View11.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View12.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View2.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View3.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View4.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View5.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View6.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View7.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View8.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/View9.qml
/usr/share/qt5/examples/charts/qmlchart/qml/qmlchart/main.qml
/usr/share/qt5/examples/charts/qmlchart/qmlchart.pro
/usr/share/qt5/examples/charts/qmlchart/resources.qrc
/usr/share/qt5/examples/charts/qmlcustomizations/main.cpp
/usr/share/qt5/examples/charts/qmlcustomizations/qml/qmlcustomizations/main.qml
/usr/share/qt5/examples/charts/qmlcustomizations/qmlcustomizations.pro
/usr/share/qt5/examples/charts/qmlcustomizations/resources.qrc
/usr/share/qt5/examples/charts/qmlcustomlegend/main.cpp
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/AnimatedAreaSeries.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/ChartViewHighlighted.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/ChartViewSelector.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/ChartViewStacked.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/CustomLegend.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qml/qmlcustomlegend/main.qml
/usr/share/qt5/examples/charts/qmlcustomlegend/qmlcustomlegend.pro
/usr/share/qt5/examples/charts/qmlcustomlegend/resources.qrc
/usr/share/qt5/examples/charts/qmlf1legends/main.cpp
/usr/share/qt5/examples/charts/qmlf1legends/qml/qmlf1legends/SpeedsXml.qml
/usr/share/qt5/examples/charts/qmlf1legends/qml/qmlf1legends/main.qml
/usr/share/qt5/examples/charts/qmlf1legends/qmlf1legends.pro
/usr/share/qt5/examples/charts/qmlf1legends/resources.qrc
/usr/share/qt5/examples/charts/qmloscilloscope/datasource.cpp
/usr/share/qt5/examples/charts/qmloscilloscope/datasource.h
/usr/share/qt5/examples/charts/qmloscilloscope/main.cpp
/usr/share/qt5/examples/charts/qmloscilloscope/qml/qmloscilloscope/ControlPanel.qml
/usr/share/qt5/examples/charts/qmloscilloscope/qml/qmloscilloscope/MultiButton.qml
/usr/share/qt5/examples/charts/qmloscilloscope/qml/qmloscilloscope/ScopeView.qml
/usr/share/qt5/examples/charts/qmloscilloscope/qml/qmloscilloscope/main.qml
/usr/share/qt5/examples/charts/qmloscilloscope/qmloscilloscope.pro
/usr/share/qt5/examples/charts/qmloscilloscope/resources.qrc
/usr/share/qt5/examples/charts/qmlpiechart/main.cpp
/usr/share/qt5/examples/charts/qmlpiechart/qml/qmlpiechart/main.qml
/usr/share/qt5/examples/charts/qmlpiechart/qmlpiechart.pro
/usr/share/qt5/examples/charts/qmlpiechart/resources.qrc
/usr/share/qt5/examples/charts/qmlpolarchart/main.cpp
/usr/share/qt5/examples/charts/qmlpolarchart/qml/qmlpolarchart/View1.qml
/usr/share/qt5/examples/charts/qmlpolarchart/qml/qmlpolarchart/View2.qml
/usr/share/qt5/examples/charts/qmlpolarchart/qml/qmlpolarchart/View3.qml
/usr/share/qt5/examples/charts/qmlpolarchart/qml/qmlpolarchart/main.qml
/usr/share/qt5/examples/charts/qmlpolarchart/qmlpolarchart.pro
/usr/share/qt5/examples/charts/qmlpolarchart/resources.qrc
/usr/share/qt5/examples/charts/qmlweather/main.cpp
/usr/share/qt5/examples/charts/qmlweather/qml/qmlweather/main.qml
/usr/share/qt5/examples/charts/qmlweather/qmlweather.pro
/usr/share/qt5/examples/charts/qmlweather/resources.qrc
/usr/share/qt5/examples/charts/scatterchart/chartview.cpp
/usr/share/qt5/examples/charts/scatterchart/chartview.h
/usr/share/qt5/examples/charts/scatterchart/main.cpp
/usr/share/qt5/examples/charts/scatterchart/scatterchart.pro
/usr/share/qt5/examples/charts/scatterinteractions/chartview.cpp
/usr/share/qt5/examples/charts/scatterinteractions/chartview.h
/usr/share/qt5/examples/charts/scatterinteractions/main.cpp
/usr/share/qt5/examples/charts/scatterinteractions/scatterinteractions.pro
/usr/share/qt5/examples/charts/splinechart/main.cpp
/usr/share/qt5/examples/charts/splinechart/splinechart.pro
/usr/share/qt5/examples/charts/stackedbarchart/main.cpp
/usr/share/qt5/examples/charts/stackedbarchart/stackedbarchart.pro
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/drilldownchart.cpp
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/drilldownchart.h
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/drilldownseries.cpp
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/drilldownseries.h
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/main.cpp
/usr/share/qt5/examples/charts/stackedbarchartdrilldown/stackedbarchartdrilldown.pro
/usr/share/qt5/examples/charts/temperaturerecords/main.cpp
/usr/share/qt5/examples/charts/temperaturerecords/temperaturerecords.pro
/usr/share/qt5/examples/charts/zoomlinechart/chart.cpp
/usr/share/qt5/examples/charts/zoomlinechart/chart.h
/usr/share/qt5/examples/charts/zoomlinechart/chartview.cpp
/usr/share/qt5/examples/charts/zoomlinechart/chartview.h
/usr/share/qt5/examples/charts/zoomlinechart/main.cpp
/usr/share/qt5/examples/charts/zoomlinechart/zoomlinechart.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Charts.so.5
/usr/lib64/libQt5Charts.so.5.15
/usr/lib64/libQt5Charts.so.5.15.17
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
