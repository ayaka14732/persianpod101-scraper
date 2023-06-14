<h1 align="center">:zap: persianpod101-scraper	:zap:</h1>

## :mortar_board: About

persianpod101-scraper helps you download Persian language courses and save them to a local directory.
The course is produced and distributed by [Innovative Language](https://www.innovativelanguage.com/online-language-courses),
who provides language learning courses from a selection of dozens of languages. Each lesson is usually 10-20 minutes long.

To get started, [choose the Persian course](https://www.innovativelanguage.com/online-language-courses)
offered by Innovative Language and create a free account.

## :pushpin: Usage

To use the script, fulfill the requirements and follow the example as demonstrated below.

### :electric_plug: Requirements

- Download and install [Python 3.9+](https://www.python.org/).
- Install required packages from [`requirements.txt`](requirements.txt) file using
  [pip](https://packaging.python.org/tutorials/installing-packages/).

  ```sh
  pip install -r requirements.txt
  ```
- Put your username and password in [`scrape.py`](scrape.py).
- Run the scraping script:

  ```sh
  python scrape.py
  ```

  The scraped file is already stored in [`data.csv`](data.csv).
- Run the post-processing script:

  ```sh
  python postprocess.py
  ```

## :clipboard: Disclaimer and known issues

- Any usage of the script is under the user's responsibility only. Users of the script must act according to the site's terms.

- As of today, Innovative Language's terms of use do not forbid the usage of crawlers or scrapers on any of their sites.
This may change in the future, so be aware.

- If you like the services Innovative Language provides you should consider a monthly subscription. Basic programs start at around $5 per month and include support from native speaker teachers.

- As with all websites, the site's structure may change in the future and thus, as often happens with scraping scripts, deprecate it. It is not really a question of *if* the site's source code will change but rather **when** (so enjoy it while it's still working :grin:).

## :lock: License

All of the content presented on the websites belongs to the original creators (Innovative Language) and I have nothing to do with it.

The license below refers only to the script and not to the downloaded content.

[License - MIT](LICENSE.md)

## :speech_balloon: Status and changelog

- **15.06.2023**:
Adapt to [persianpod101.com](https://www.persianpod101.com/).
- **23.03.2022**:
Added support for basic video downloading (nothing fancy, just m4v and mp4 files)
Added error handling for when a lesson library/lesson contents URL is used instead of the first lesson (user is now warned)
- **11.05.2021**:
Headers and waiting time added, script is alive again.
