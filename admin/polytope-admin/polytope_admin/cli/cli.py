#
# Copyright 2022 European Centre for Medium-Range Weather Forecasts (ECMWF)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

"""This is the source code of a Command Line Interface
that sends HTTP requests behind the scenes to communicate
with the RESTful API exposed by a Polytope frontend."""

import click

from ..version import __version__
from . import binders

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__)
def cli():
    pass


@cli.group()
def set():
    pass


set.add_command(binders.config.set, name="config")
set.add_command(binders.auth.set, name="credentials")


@cli.group()
def unset():
    pass


unset.add_command(binders.config.unset, name="config")
unset.add_command(binders.auth.unset, name="credentials")


@cli.group()
def list():
    pass


list.add_command(binders.config.list, name="config")
list.add_command(binders.auth.list, name="credentials")


@cli.group()
def create():
    pass


create.add_command(binders.admin.create, name="user")


@cli.group()
def delete():
    pass


delete.add_command(binders.admin.delete, name="user")

cli.add_command(binders.auth.login, name="login")
cli.add_command(binders.admin.ping, name="ping")

if __name__ == "__main__":
    cli()
