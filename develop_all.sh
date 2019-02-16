#!/usr/bin/env bash

cd entry_points_base
python setup.py develop
cd ../entry_points_expensive/
python setup.py develop
cd ../entry_points_health/
python setup.py develop
cd ../entry_points_ready/
python setup.py develop
cd ../end_product/
python setup.py develop
cd ../end_product_expensive/
python setup.py develop
cd ..
