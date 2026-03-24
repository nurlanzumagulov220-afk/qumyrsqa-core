from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical
import winsound
import asyncio

class SwarmLiveApp(App):
    CSS = """
    Static { border: double green; padding: 1; margin: 1; color: #00ff00; }
    .best-choice { border: double yellow; color: yellow; text-style: bold; }
    .status-bar { background: #002200; text-align: center; }
    """

    # Начальные данные
    dist = 5.0
    v_id = "Самосвал-05"

    def on_mount(self) -> None:
        # Приветственный сигнал
        winsound.Beep(1000, 150)
        winsound.Beep(1200, 200)
        # Запускаем обновление данных каждую секунду
        self.set_interval(1, self.update_distance)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical():
            yield Static("🛡️ GUARD AI & ISU SWARM | ПРЕДИКТИВНАЯ ЛОГИСТИКА", classes="status-bar")
            yield Static(f"📍 ЦЕЛЬ: Скважина №5 | ПРИОРИТЕТ: Высокий")
            # Эти виджеты мы будем обновлять
            self.display_dist = Static(f"🤖 АНАЛИЗ РОЯ: {self.v_id} в пути...")
            self.display_info = Static(f"✅ ДИСТАНЦИЯ: {self.dist} км", classes="best-choice")
            yield self.display_dist
            yield self.display_info
        yield Footer()

    def update_distance(self) -> None:
        # Уменьшаем дистанцию, имитируя движение
        if self.dist > 0.1:
            self.dist = round(self.dist - 0.1, 1)
            self.display_info.update(f"✅ ДИСТАНЦИЯ: {self.dist} км")
        else:
            self.display_info.update("🏁 ТЕХНИКА ПРИБЫЛА НА ОБЪЕКТ!")
            self.display_info.styles.color = "lightgreen"

if __name__ == "__main__":
    app = SwarmLiveApp()
    app.run()