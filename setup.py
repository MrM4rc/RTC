import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="rtc", # Replace with your own username
	version="1.0",
	author="MrM4rc",
	author_email="marcelorap345@gmail.com",
	description="rtc is a real-time chat.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="~",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
