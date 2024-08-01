from typing import Optional
from enum import Enum

from pydantic import BaseModel, conlist, Field

from aiogram.filters.callback_data import CallbackData


class SimpleCalAct(str, Enum):
    ignore = 'IGNORE'
    prev_y = 'PREV-YEAR'
    next_y = 'NEXT-YEAR'
    prev_m = 'PREV-MONTH'
    next_m = 'NEXT-MONTH'
    cancel = 'CANCEL'
    today = 'TODAY'
    day = 'DAY'


class DialogCalAct(str, Enum):
    ignore = 'IGNORE'
    set_y = 'SET-YEAR'
    set_m = 'SET-MONTH'
    prev_y = 'PREV-YEAR'
    next_y = 'NEXT-YEAR'
    cancel = 'CANCEL'
    start = 'START'
    day = 'SET-DAY'


class CalendarCallback(CallbackData, prefix="calendar"):
    act: str
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None


class SimpleCalendarCallback(CalendarCallback, prefix="simple_calendar"):
    act: SimpleCalAct


class DialogCalendarCallback(CalendarCallback, prefix="dialog_calendar"):
    act: DialogCalAct


class CalendarLabels(BaseModel):
    "Schema to pass labels for calendar. Can be used to put in different languages"
    days_of_week: conlist(str, max_length=7, min_length=7) = ["Пон", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    months: conlist(str, max_length=12, min_length=12) = [
        "Янв", "Фев", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сент", "Окт", "Ноя", "Дек"
    ]
    cancel_caption: str = Field(default='Отмена', description='Caption for Cancel button')
    today_caption: str = Field(default='Сегодня', description='Caption for Today button')



HIGHLIGHT_FORMAT = "[{}]"
SELECTED_FORMAT = "{}➡️"


def highlight(text):
    return HIGHLIGHT_FORMAT.format(text)

def selected(text):
    return SELECTED_FORMAT.format(text)

def superscript(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    output = ''
    for i in text:
        output += (super_s[normal.index(i)] if i in normal else i)
    return output

def subscript(text):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    output = ''
    for i in text:
        output += (sub_s[normal.index(i)] if i in normal else i)
    return output
