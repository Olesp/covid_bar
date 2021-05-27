# Title / Repository Name

## About / Synopsis

* This is a xbar plugin to display key numbers about covid in the country of your choice
* Project status: working/prototype

## Table of contents

> * [Title / Repository Name](#title--repository-name)
>   * [About / Synopsis](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>     * [Screenshots](#screenshots)
>     * [Features](#features)
>   * [Code](#code)
>     * [Content](#content)
>     * [Requirements](#requirements)
>     * [Limitations](#limitations)
>     * [Build](#build)
>     * [Deploy (how to install build product)](#deploy-how-to-install-build-product)
>   * [Resources (Documentation and other links)](#resources-documentation-and-other-links)
>   * [Contributing / Reporting issues](#contributing--reporting-issues)
>   * [License](#license)
>   * [About Nuxeo](#about-nuxeo)

## Installation

Sample:

* Install the xbar app from this [link](https://github.com/matryer/xbar)
* Download the covid_daily.60m.py file and place it into the xbar plugins folder
* Get your api key from the [rapidapi website](https://rapidapi.com/Gramzivi/api/covid-19-data)
* Place the api key into the xvar field
* Write the country name of your choice in the dedicated xvar Field 
* Use the ``chmod +x `` to make the file executable
* Refresh the plugin from the xbar icon at the top

## Usage
Simply click the icon to display key numbers about the covid in the country
### Screenshots
![alt](https://i.ibb.co/dQ6NSmJ/Capture-d-e-cran-2021-05-27-a-14-50-07.png)
### Features
* Total cases in the country
* Total deaths in the country
* Recovery cases in the country

### Content

Description, sub-modules organization...

### Requirements

1. Python3
2. Requests lib
3. Api key from rapidapi.com
4. xbar installed