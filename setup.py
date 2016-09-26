#!/usr/bin/env python
# encoding: utf-8

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


setup(
		name = "WebCore-Wiki-Tutorial",
		version = "0.1",
		
		description = "An example Wiki application for WebCore.",
		long_description = "",
		url = "https://github.com/marrow/tutorial",
		author = "Alice Bevan-McGregor",
		author_email = "alice@gothcandy.com",
		license = "mit",
		keywords = [],
		
		packages = find_packages(exclude=['test', 'example', 'conf', 'benchmark', 'tool', 'doc']),
		include_package_data = True,
		package_data = {'': [
				'README.rst',
				'LICENSE.txt'
			]},
		
		namespace_packages = [
				'web',
				'web.app',
			],
		
		setup_requires = [
				'pytest-runner',
			],
		
		tests_require = [
				'pytest-runner',
				'coverage',
				'pytest',
				'pytest-cov',
				'pytest-spec',
				'pytest-flakes',
			],
		
		install_requires = [
				'WebCore>=2.0.3,<3',  # The underlying web framework.
				'web.db',  # Database connectivity layer for WebCore.
				'marrow.mongo',  # Database connectivity and schema + query system for MongoDB.
				'web.dispatch.object',  # Object (class-based filesystem-like) dispatch for endpoint discovery.
				'web.dispatch.resource',  # Resource (based on REQUEST_METHOD) dispatch for endpoint discovery.
				'cinje',  # Template engine, an importable Python domain-specific code transformer / language.
			],
		
		extras_require = dict(
				development = [
						'pytest-runner',
						'coverage',
						'pytest',
						'pytest-cov',
						'pytest-spec',
						'pytest-flakes',
					],
			),
		
		entry_points = {
				}
	)
