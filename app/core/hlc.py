import time
import threading

class HybridLogicalClock:
    def __init__(self):
        self.l = 0  # Максимальное физическое время (мс), которое мы видели
        self.c = 0  # Логический счетчик для событий в ту же миллисекунду
        self._lock = threading.Lock()

    def _now(self):
        """Получаем текущее системное время в миллисекундах."""
        return int(time.time() * 1000)

    def generate_timestamp(self):
        """Создает новую метку времени для локального события (Amanat Ledger)."""
        with self._lock:
            pt = self._now()
            if pt > self.l:
                self.l = pt
                self.c = 0
            else:
                self.c += 1
            
            return (self.l, self.c)

    def observe(self, remote_l, remote_c):
        """Обновляет локальные часы при получении события от другого участника Роя."""
        with self._lock:
            pt = self._now()
            old_l = self.l
            
            # Правило HLC: берем максимум из локального, удаленного и системного времени
            self.l = max(old_l, remote_l, pt)
            
            if self.l == old_l and self.l == remote_l:
                self.c = max(self.c, remote_c) + 1
            elif self.l == old_l:
                self.c += 1
            elif self.l == remote_l:
                self.c = remote_c + 1
            else:
                self.c = 0
                
            return (self.l, self.c)

    def to_string(self, ts):
        """Превращает кортеж (l, c) в красивую строку для реестра."""
        return f"{ts[0]}:{ts[1]}"

# Глобальный экземпляр для использования в приложении
amanat_clock = HybridLogicalClock()