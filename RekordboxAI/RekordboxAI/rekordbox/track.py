from dataclasses import dataclass
from typing import Optional

from rekordbox.position_mark import PositionMark
from rekordbox.tempo import Tempo


@dataclass
class Track:
    def __init__(
        self,
        track_id:       Optional[int],
        name:           Optional[str],
        artist:         Optional[str],
        composer:       Optional[str],
        album:          Optional[str],
        grouping:       Optional[str],
        genre:          Optional[str],
        kind:           Optional[str],
        size:           Optional[int],
        total_time:     Optional[float],
        disc_number:    Optional[int],
        track_number:   Optional[int],
        year:           Optional[int],
        average_bpm:    Optional[float],
        date_modified:  Optional[str],
        date_added:     Optional[str],
        bit_rate:       Optional[int],
        sample_rate:    Optional[float],
        comments:       Optional[str],
        play_count:     Optional[int],
        last_played:    Optional[str],
        rating:         Optional[int],
        location:       Optional[str],
        remixer:        Optional[str],
        tonality:       Optional[str],
        label:          Optional[str],
        mix:            Optional[str],
        colour:         Optional[str],
        tempo:          Optional[Tempo],
        position_mark:  Optional[PositionMark],
        ):
        self.track_id       = track_id
        self.name           = name
        self.artist         = artist
        self.composer       = composer
        self.album          = album
        self.grouping       = grouping
        self.genre          = genre
        self.kind           = kind
        self.size           = size
        self.total_time     = total_time
        self.disc_number    = disc_number
        self.track_number   = track_number
        self.year           = year
        self.average_bpm    = average_bpm
        self.date_modified  = date_modified
        self.date_added     = date_added
        self.bit_rate       = bit_rate
        self.sample_rate    = sample_rate
        self.comments       = comments
        self.play_count     = play_count
        self.last_played    = last_played
        self.rating         = rating
        self.location       = location
        self.remixer        = remixer
        self.tonality       = tonality
        self.label          = label
        self.mix            = mix
        self.colour         = colour
        self.tempo          = tempo
        self.position_mark  = position_mark