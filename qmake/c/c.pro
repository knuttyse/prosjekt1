TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp

INCLUDEPATH =/usr/include
LIBS += -larmadillo -llapack -lblas
