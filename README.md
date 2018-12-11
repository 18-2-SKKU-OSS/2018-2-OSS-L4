# MusicBot

**이 브랜치는...**

이 Musicbot의 브랜치는 `rewrite` 버전의 discord.py 라이브러리와만 호환 가능합니다. 해당 라이브러리는 `python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]`로 설치 가능합니다. 또한 `requirements.txt`의 목록을 dependency로 가지고 있습니다. 이것들은 bot을 설치할 때 `update.py`를 실행하면 자동으로 설치됩니다.

---

[![GitHub release](https://img.shields.io/github/release/Just-Some-Bots/MusicBot.svg?style=flat-square)](https://just-some-bots.github.io/MusicBot/)
[![Python](https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Discord](https://discordapp.com/api/guilds/129489631539494912/widget.png?style=shield)](https://discord.gg/bots)

MusicBot은 [Python](https://www.python.org "Python homepage") 3.5+로 짜여진 디스코드 음악 봇입니다. [discord.py](https://github.com/Rapptz/discord.py)라이브러리를 사용합니다. 이 봇은 하나 이상의 디스코드 서버에 유튜브나 기타 플랫폼에서 요청받은 음악을 재생합니다. 만약 요청 큐가 비었다면 재생 리스트에서 음악을 재생하게 설정할 수 있습니다. 봇의 소유자는 봇이 특정 사람의 명령어만 받아들이게 제한할 수 있습니다. MusicBot은 음악 재생뿐만 아니라 라이브 미디어를 음성 채널로 스트리밍 할 수 있습니다. 이는 아직 미완성된 기능입니다.

![Main](https://i.imgur.com/EZljY52.png)

## 설정
MusicBot을 설치하는 것은 굉장히 쉽습니다. 우리가 준비한 이 [가이드](https://just-some-bots.github.io/MusicBot/)만 따라하면 됩니다. 가이드를 따라 한 뒤에, 디스코드에 봇을 연결하기 위한 설정을 시작하면 됩니다.

가장 중요한 설정 파일은 `config/options.ini`이지만 이 파일은 레포지토리에 포함되어 있지 않습니다. `example_options.ini`의 이름을 `options.ini`로 바꾸세요. `example_options.ini` 에 설정을 위한 더 많은 정보들이 적혀져 있습니다.

### 명령어들

봇을 위해 굉장히 많은 명령어들이 있습니다. 가장 중요한 명령어는 `play <url>` 입니다(preceded by your command prefix). 이 명령어는 유튜브나 다른 플랫폼에서 음악을 다운로드하고 플레이합니다. 모든 명령어를 보려면 [여기](https://just-some-bots.github.io/MusicBot/using/commands/ "Commands")를 클릭하세요.

### 추가적인 문서

* [Support Discord server](https://discord.gg/bots)
* [Project license](LICENSE)
