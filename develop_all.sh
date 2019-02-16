#!/usr/bin/env bash

cd base
python setup.py develop
cd ../health_plugin/
python setup.py develop
cd ../ready_plugin/
python setup.py develop
cd ../expensive_plugin/
python setup.py develop
cd ../end_product/
python setup.py develop
cd ..
