import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import CostKpi, DurationKpi, AccKpi

train_cost_kpi = AccKpi('train_cost', 0.05, 0)
train_speed_kpi = AccKpi('train_speed', 0.05, 0)


tracking_kpis = [
	train_cost_kpi,
	train_speed_kpi
]