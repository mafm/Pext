#!/usr/bin/env python3

# Copyright (c) 2016 - 2017 Sylvia van Os <sylvia@hackerchick.me>
#
# This file is part of Pext
#
# Pext is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Pext Helpers.

This file contains various functionality that is relevant to both Pext
and modules and helps keep the API consistent.
"""

from enum import Enum


class Action(Enum):
    """Introduced in API version 0.1.0.

    The list of actions a module can request.

    A module can request any of these actions of the core by putting it in the
    queue. All of these actions need to be accompanied by a list of arguments.
    In these examples, we assume that you have assigned the queue variable to
    self.q, a common practice in Pext modules.

    critical_error
        Introduced in API version 0.1.0.

        Show an error message on the screen and unload the module.
        This function is also called when the module throws an exception.

        message -- error message to show

        Example: self.q.put([Action.critical_error, "Something went wrong!"])

    add_message
        Introduced in API version 0.1.0.

        Show a message on the screen.

        message -- message to show

        Example: self.q.put([Action.add_message, "We did a thing"])

    add_error
        Introduced in API version 0.1.0.

        Show an error message on the screen.

        message -- error message to show

        Example: self.q.put([Action.add_error, "We did a thing, but it went wrong"])

    add_entry
        Introduced in API version 0.1.0.
        Changed in API version 0.8.0.

        Add an entry to the entry list.

        entry -- an instance of Entry

        Example: self.q.put([Action.add_entry, entry("Audio settings")])

    prepend_entry
        Introduced in API version 0.1.0.
        Changed in API version 0.8.0.

        Prepend an entry to the entry list.

        entry -- an instance of Entry

        Example: self.q.put([Action.prepend_entry, entry("volume", type=SelectionType.command)])

    remove_entry
        Introduced in API version 0.1.0.
        Changed in API version 0.8.0.

        Remove an entry from the entry list.

        entry -- an instance of Entry

        Example: self.q.put([Action.remove_entry, entry])

    clear_entries
        Introduced in API version 0.8.0.

        Clear the list of enries.

        Example: self.q.put([Action.clear_entry_list])

    set_header
        Introduced in API version 0.1.0.

        Set or replace the text currently in the header bar.

        If header is not given, the header will be removed.

        header -- the new header text

        Example: self.q.put([Action.set_header, "Weather for New York"])

    set_filter
        Introduced in API version 0.1.0.

        Replace the text currently in the search bar.

        filter -- the new text to put in the search bar

        Example: self.q.put([Action.set_header, "Weather for New York"])

    ask_question_default_yes
        Introduced in API version 0.1.0.

        Ask a yes/no question, with the default value being yes.

        question -- the question to ask
        identifier -- an optional identifier which gets passed back to process_response

        Example: self.q.put([Action.ask_question_default_yes, "Are you sure you want to continue?", 0])

    ask_question_default_no
        Introduced in API version 0.1.0.

        Ask a yes/no question, with the default value being no.

        question -- the question to ask
        identifier -- an optional identifier which gets passed back to process_response

        Example: self.q.put([Action.ask_question_default_no, "Are you sure you want to continue?", 0])

    ask_input
        Introduced in API version 0.1.0.
        Changed in API version 0.2.0.

        Ask the user to input a single line of text.

        text -- the text to show the user
        prefill -- the text to already put into the input field
        identifier -- an optional identifier which gets passed back to process_response

        Example: self.q.put([Action.ask_input, "Please choose a new name for this entry", "Example name", 0])

    ask_input_password:
        Introduced in API version 0.1.0.
        Changed in API version 0.2.0.

        Ask the user to input a single line of text into a password field.

        text -- the text to show the user
        prefill -- the text to already put into the input field (hidden behind asterisks, of course)
        identifier -- an optional identifier which gets passed back to process_response

        Example: self.q.put([Action.ask_input_password, "Please enter your password", "Current password", 0])

    ask_input_multi_line
        Introduced in API version 0.1.0.

        Ask the user to input one or more lines of text.

        text -- the text to show the user
        prefill -- the text to already put into the input field
        identifier -- an optional identifier which gets passed back to process_response

        The prefill may contain newline characters.

        Example: self.q.put([Action.ask_input_multi_line, "List your favourite animals", "Cat and dog", 0])

    copy_to_clipboard
        Introduced in API version 0.1.0.

        Copy data to the clipboard.

        text -- the text to copy to the clipboard

        Example: self.q.put([Action.copy_to_clipboard, "I like Pext"])

    set_selection
        Introduced in API version 0.1.0.

        Change the internal Pext selection for this module.

        The internal Pext selection contains a list of all entries the user
        chose since the last time the window was closed.

        To go a single level up, simply remove the last entry from this list.
        To reset to the main screen, use an empty list.

        After set_selection is called, selection_made in ModuleBase will be
        called with the new values.

        list -- the selection list

        Example: self.q.put([Action.set_selection, [entry1, entry2])

    close:
        Introduced in API version 0.1.0.

        Close the window.

        Call this when the user is done. For example, when the user made a
        selection.

        Example: self.q.put([Action.close])

    set_base_info:
        Introduced in API version 0.6.

        Set an info block to always show regardless of the active selection.

        Example: self.q.put([Action.set_base_info, "Type stop to stop listening to radio"])

    set_base_context:
        Introduced in API version 0.6.

        Set the base context, reachable by right-clicking the header text or Ctrl+Shift+..

        Example: self.q.put([Action.set_base_context, ["Mute", "Stop"]])

    """

    critical_error = 0
    add_message = 1
    add_error = 2
    add_entry = 3
    prepend_entry = 4
    remove_entry = 5
    clear_entries = 6
    set_header = 7
    set_filter = 8
    ask_question_default_yes = 9
    ask_question_default_no = 10
    ask_input = 11
    ask_input_password = 12
    ask_input_multi_line = 13
    set_selection = 14
    close = 15
    set_base_info = 16
    set_base_context = 17


class ModuleGlobal():
    """Introduced in API version 0.8.0.

    header
        Introduced in API version 0.8.0.

        The header that will be shown when no entry in the history overwrites it.

        If not given, defaults to None.

    options
        Introduced in API version 0.8.0.

        The list of options available.

        If not given, defaults to an empty list.

    info_html
        Introduced in API version 0.8.0.

        The extra info to display, formatted as HTML.

        If not given, defaults to an entry string.
    """

    def __init__(self, header=None, options=[], info_html="") -> None:
        """Create a new instance of ModuleGlobal."""
        self.header = header
        self.options = options
        self.info_html = info_html

    @property
    def header(self):
        """Return the header to display."""
        return self._header

    @property
    def options(self):
        """Return the list of options."""
        return self._options

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def info_html(self):
        """Return the list of additional HTML-formatted info."""
        return self._info_html

    @options.setter
    def options(self, value):
        self._options = value

    @info_html.setter
    def info_html(self, value):
        self._info_html = value


class EntryType(Enum):
    """Introduced in API version 0.8.0.

    A list of possible selection types.

    entry
        Introduced in API version 0.8.0.

        An entry which will cause selection_made to be called when selected.

    copyable
        Introduced in API version 0.8.0.

        An entry which will be copied to the clipboard when selected.
    """

    entry = 0
    copyable = 1


class Entry():
    """Introduced in API version 0.8.0.

    name
        Introduced in API version 0.8.0.

        The string name of the entry.

    copyname
        Introduced in API version 0.8.0.

        If not None, the string that will be copied to the clipboard if the entry is of type copyable.
        If None, but the entry type is copyable, the name will be copied instead.

        If not given, defaults to None

    type
        Introduced in API version 0.8.0.

        An instance of EntryType.

        If not given, defaults to EntryType.entry.

    options
        Introduced in API version 0.8.0.

        The list of options available for an entry.

        If not given, defaults to an empty list.

    info_html
        Introduced in API version 0.8.0.

        The extra info for an entry, formatted as HTML.

        If not given, defaults to an entry string.

    header
        Introduced in API version 0.8.0.

        The header that will be shown when this entry is in the history.

        If None, will bubble up until an entry with a header is found.

        Set to an empty string to explicitly overwrite any previous header with emptiness.

        If not given, defaults to None.

    module_internal
        Introduced in API version 0.8.0.

        This field can contain any info a module wishes, Pext will never touch it.

        Useful for storing extra (hidden) data.

        If not given, defaults to none.
    """

    def __init__(self, name, copyname=None, type=EntryType.entry, options=[], info_html="", header=None,
                 module_internal=None) -> None:
        """Create a new entry, with name and optional other settings."""
        self.name = name
        self.copyname = copyname
        self.type = type
        self.options = options
        self.info_html = info_html
        self.header = header
        self.module_internal = module_internal

    @property
    def name(self):
        """Return the name of the entry."""
        return self._name

    @property
    def copyname(self):
        """Return the name that will be copied to the clipboard if copyable of the entry."""
        return self._copyname

    @property
    def type(self):
        """Return the EntryType of the entry."""
        return self._type

    @property
    def options(self):
        """Return the list of options of the entry."""
        return self._options

    @property
    def info_html(self):
        """Return the list of additional HTML-formatted info for the entry."""
        return self._info_html

    @property
    def header(self):
        """Return the header to display."""
        return self._header

    @property
    def module_internal(self):
        """Return the hidden data the module added."""
        return self._module_internal

    @name.setter
    def name(self, value):
        self._name = value

    @copyname.setter
    def copyname(self, value):
        self._copyname = value

    @type.setter
    def type(self, value):
        if not isinstance(value, EntryType):
            raise ValueError("{} is not part of EntryType enum".format(value))

        self._type = value

    @options.setter
    def options(self, value):
        self._options = value

    @info_html.setter
    def info_html(self, value):
        self._info_html = value

    @header.setter
    def header(self, value):
        self._header = value

    @module_internal.setter
    def module_internal(self, value):
        self._module_internal = value


class Selection():
    """Introduced in API version 0.8.0.

    entry
        Introduced in API version 0.8.0.

        An entry if the selection relates to any specific entry, otherwise None.

    option
        Introduced in API version 0.8.0.

        An option if selected, otherwise None.
    """

    def __init__(self, entry=None, option=None) -> None:
        """Create a new instance of Selection."""
        self.entry = entry
        self.option = option

    @property
    def entry(self):
        """Return the selected entry, if any."""
        return self._entry

    @property
    def option(self):
        """Return the selected option, if any."""
        return self._option

    @entry.setter
    def entry(self, value):
        if not isinstance(value, Entry):
            raise ValueError("{} is not of the type Entry".format(value))

        self._entry = value

    @option.setter
    def option(self, value):
        self._option = value
