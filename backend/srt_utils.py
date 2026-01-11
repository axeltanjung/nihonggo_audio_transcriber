def format_time(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02}:{m:02}:{s:06.3f}".replace(".", ",")


def segments_to_srt(segments):
    lines = []
    for i, s in enumerate(segments, 1):
        lines.append(str(i))
        lines.append(f"{format_time(s['start'])} --> {format_time(s['end'])}")
        lines.append(s["text"].strip())
        lines.append("")
    return "\n".join(lines)
