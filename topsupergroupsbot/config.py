# TopSupergroupsBot - A telegram bot for telegram public groups leaderboards
# Copyright (C) 2017  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)
#
# TopSupergroupsBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TopSupergroupsBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with TopSupergroupsBot.  If not, see <http://www.gnu.org/licenses/>.


import yaml
import sys


path = "config/config.yaml"
if len(sys.argv) == 2:
    path = sys.argv[1]
try:
    with open(path, 'r') as stream:
        conf = yaml.load(stream)
except FileNotFoundError:
    print("\n\WARNING:\n"
            "before of running topsupergroupsbot you should create a file named `config.yaml`"
            " in `config`.\n\nOpen `config/config.example.yaml`\ncopy all\ncreate a file "
            "named `config.yaml`\nPaste and replace sample variables with true data."
            "\nIf the file is in another path, you can specify it as the first parameter."
            "\nExample: <topsupergroupsbot /home/my_files/config.yaml>")
    sys.exit()


BOT_TOKEN = conf["bot_token"]
POSTGRES_DB = conf["postgres_db"]

REDIS_HOST = conf["redis_host"]
REDIS_PORT = conf["redis_port"]
REDIS_DB = conf["redis_db"]

ADMINS = conf["admins"]

FOUNDER = conf["founder"]

FLOOD_CHECKS = conf["flood_checks"]
