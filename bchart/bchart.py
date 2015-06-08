# -*- coding: utf-8 -*-
"""
bCharts: Constructors for all different charts from bChart.
"""

import json

class bChart(object):
	"""Abstract Base Class for all Chart types"""
	def __init__(self, selector=None, chartType=None, options=None):
		if options is None:
			if chartType is None:
				self.options = {}
			# elif chartType == "area":
			# 	with open("./json/area.json", "w") as f:
			# 		print f
			# 		self.options = f
		else: 
			self.options = options

		if selector is None:
			raise ValueError("Please initialize the chart with a CSS selector")
		else:
			self.selector = selector
			self.options['selector'] = self.selector

		if chartType is None:
			raise ValueError("Please initialize the chart type!")
		else:
			self.chartType = chartType
			self.options['chartType'] = self.chartType

	def load(self, data=None):
		if data is None:
			raise ValueError("Please load a 2-dimension list or an json style object")
		else:
			if isinstance(data,list):
				if not isinstance(data[0], list):
					raise ValueError("Please load a 2-dimension list")
				else:
					if not "data" in self.options:
						self.options['data'] = {
							"dataValue": [],
							"groups": [],
							"groups2": [],
							"x": []
						}
					for i in range(0,len(data)):
						self.options['data']['dataValue'].append([])
						# print i
						for j in data[i]:
							self.options['data']['dataValue'][i].append(j)
			else:
				self.options.data = data;
		return self

	def unload(self, groupList=None):
		if groupList is None or not isinstance(groupList, list):
			raise ValueError("Please load a list of data name to unload data")
		else:
			self.options.unloadData = groupList
		return self

	def colors(self, colorList=None):
		if colorList is None:
			return self.options['colors']
		else:
			if not isinstance(colorList, list):
				raise ValueError("Please input a list of colors.")
			else:
				self.options['colors'] = colorList
		return self

	def legend(self, propertyKey=None, propertyValue=None):
		if not "legend" in self.options:
			self.options["legend"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["legend"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["legend"] = propertyKey
			else:
				self.options["legend"][propertyKey] = propertyValue
		return self

	def background(self, propertyKey=None, propertyValue=None):
		if not "background" in self.options:
			self.options["background"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["background"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["background"] = propertyKey
			else:
				self.options["background"][propertyKey] = propertyValue
		return self

	def tooltip(self, propertyKey=None, propertyValue=None):
		if not "tooltip" in self.options:
			self.options["tooltip"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["tooltip"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["tooltip"] = propertyKey
			else:
				self.options["tooltip"][propertyKey] = propertyValue
		return self

	def xAxis(self, propertyKey=None, propertyValue=None):
		if not "xAxis" in self.options:
			self.options["xAxis"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["xAxis"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["xAxis"] = propertyKey
			else:
				self.options["xAxis"][propertyKey] = propertyValue
		return self

	def yAxis(self, propertyKey=None, propertyValue=None):
		if not "yAxis" in self.options:
			self.options["yAxis"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["yAxis"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["yAxis"] = propertyKey
			else:
				self.options["yAxis"][propertyKey] = propertyValue
		return self

	def xLabel(self, propertyKey=None, propertyValue=None):
		if not "xLabel" in self.options:
			self.options["xLabel"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["xLabel"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["xLabel"] = propertyKey
			else:
				self.options["xLabel"][propertyKey] = propertyValue
		return self

	def yLabel(self, propertyKey=None, propertyValue=None):
		if not "yLabel" in self.options:
			self.options["yLabel"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["yLabel"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["yLabel"] = propertyKey
			else:
				self.options["yLabel"][propertyKey] = propertyValue
		return self

	def yAxis2(self, propertyKey=None, propertyValue=None):
		if not "yAxis2" in self.options:
			self.options["yAxis2"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["yAxis2"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["yAxis2"] = propertyKey
			else:
				self.options["yAxis2"][propertyKey] = propertyValue
		return self

	def yLabel2(self, propertyKey=None, propertyValue=None):
		if not "yLabel2" in self.options:
			self.options["yLabel2"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["yLabel2"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["yLabel2"] = propertyKey
			else:
				self.options["yLabel2"][propertyKey] = propertyValue
		return self

	def title(self, propertyKey=None, propertyValue=None):
		if not "title" in self.options:
			self.options["title"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["title"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["title"] = propertyKey
			else:
				self.options["title"][propertyKey] = propertyValue
		return self

	def option(self, propertyKey=None, propertyValue=None):
		if propertyKey is None and propertyValue is None:
			return self.options
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					for key in propertyKey:
						self.options[key] = propertyKey[key]
			else:
				self.options[propertyKey] = propertyValue
		return self

	def max(self, value=None):
		if not "max" in self.options:
			self.options["max"] = {}
		if value is None:
			return self.options["max"]
		else:
			self.options["max"] = value

		return self

	def min(self, value=None):
		if not "min" in self.options:
			self.options["min"] = {}
		if value is None:
			return self.options["min"]
		else:
			self.options["min"] = value
		return self

	def max2(self, value=None):
		if not "max2" in self.options:
			self.options["max2"] = {}
		if value is None:
			return self.options["max2"]
		else:
			self.options["max2"] = value

		return self

	def min2(self, value=None):
		if not "min2" in self.options:
			self.options["min2"] = {}
		if value is None:
			return self.options["min2"]
		else:
			self.options["min2"] = value
		return self



	def to_json(self, filePath=None):
		if filePath is None:
			filePath = './bchart.json'
		with open(filePath, 'w') as f:
			json.dump(self.options, f)


class BarChart(bChart):
	"""Support group bar and stack bar chart"""
	def __init__(self, selector=None, options=None):
		super(BarChart, self).__init__(selector, 'bar', options)

class LineChart(bChart):
	"""Support line and multi-line chart"""
	def __init__(self, selector=None, options=None):
		super(LineChart, self).__init__(selector, 'line', options)

	def line(self, propertyKey=None, propertyValue=None):
		if not "line" in self.options:
			self.options["line"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["line"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["line"] = propertyKey
			else:
				self.options["line"][propertyKey] = propertyValue
		return self

	def node(self, propertyKey=None, propertyValue=None):
		if not "node" in self.options:
			self.options["node"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["node"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["node"] = propertyKey
			else:
				self.options["node"][propertyKey] = propertyValue
		return self

class AreaChart(bChart):
	"""Support area and stack area chart"""
	def __init__(self, selector=None, options=None):
		super(AreaChart, self).__init__(selector, 'area', options)

	def area(self, propertyKey=None, propertyValue=None):
		if not "area" in self.options:
			self.options["area"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["area"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["area"] = propertyKey
			else:
				self.options["area"][propertyKey] = propertyValue
		return self

class ScatterChart(bChart):
	"""Support scatter chart"""
	def __init__(self, selector=None, options=None):
		super(ScatterChart, self).__init__(selector, 'scatter', options)

	def node(self, propertyKey=None, propertyValue=None):
		if not "node" in self.options:
			self.options["node"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["node"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["node"] = propertyKey
			else:
				self.options["node"][propertyKey] = propertyValue
		return self

class BubbleChart(bChart):
	"""Support bubble chart"""
	def __init__(self, selector=None, options=None):
		super(BubbleChart, self).__init__(selector, 'bubble', options)

	def bubble(self, propertyKey=None, propertyValue=None):
		if not "bubble" in self.options:
			self.options["bubble"] = {}
		if propertyKey is None and propertyValue is None:
			return self.options["bubble"]
		else:
			if propertyValue is None:
				if isinstance(propertyKey, basestring):
					raise ValueError("Please input a value of the property")
				else:
					self.options["bubble"] = propertyKey
			else:
				self.options["bubble"][propertyKey] = propertyValue
		return self

class PieChart(bChart):
	"""Support for piechart"""
	def __init__(self, selector=None, options=None):
		super(PieC, self).__init__(selector, 'pie', options)
						

				
