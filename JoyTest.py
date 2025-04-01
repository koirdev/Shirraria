import pygame

pygame.init()


# Это простой класс, который поможет нам вывести данные на экран.
# Это не имеет ничего общего с джойстиками, просто вывод
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


def main():
    # Задайте ширину и высоту экрана (ширина, высота) и дайте окну имя.
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    # Используется для управления скоростью обновления экрана.
    clock = pygame.time.Clock()

    # Приготовьтесь к печати.
    text_print = TextPrint()

    # Этот словарь можно оставить как есть, так как pygame сгенерирует
    # событие pygame.JOYDEVICEADDED для каждого подключенного джойстика
    # в начале программы.
    joysticks = {}

    done = False
    while not done:
        # Этап обработки события.
        # Возможные события джойстика: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Помечаем, что мы закончили, и выходим из этого цикла.

            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                if event.button == 0:
                    joystick = joysticks[event.instance_id]
                    if joystick.rumble(0, 0.7, 500):
                        print(f"Rumble effect played on joystick {event.instance_id}")

            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            # Управление горячим подключением
            if event.type == pygame.JOYDEVICEADDED:
                # Это событие будет сгенерировано при запуске программы для каждого
                # джойстик, заполняя список без необходимости создавать их вручную.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        # Шаг рисования
        # Сначала очистите экран до белого цвета. Не ставьте другие команды рисования
        # выше, иначе они будут стерты этой командой.
        screen.fill((255, 255, 255))
        text_print.reset()

        # Получить количество джойстиков.
        joystick_count = pygame.joystick.get_count()

        text_print.tprint(screen, f"Number of joysticks: {joystick_count}")
        text_print.indent()

        # Для каждого джойстика:
        for joystick in joysticks.values():
            jid = joystick.get_instance_id()

            text_print.tprint(screen, f"Joystick {jid}")
            text_print.indent()

            # Получите имя контроллера/джойстика из ОС.
            name = joystick.get_name()
            text_print.tprint(screen, f"Joystick name: {name}")

            guid = joystick.get_guid()
            text_print.tprint(screen, f"GUID: {guid}")

            power_level = joystick.get_power_level()
            text_print.tprint(screen, f"Joystick's power level: {power_level}")

            # Обычно оси работают парами, вверх/вниз для одной и влево/вправо для другой.
            # другой. Триггеры считаются осями.
            axes = joystick.get_numaxes()
            text_print.tprint(screen, f"Number of axes: {axes}")
            text_print.indent()

            for i in range(axes):
                axis = joystick.get_axis(i)
                text_print.tprint(screen, f"Axis {i} value: {axis:>6.3f}")
            text_print.unindent()

            buttons = joystick.get_numbuttons()
            text_print.tprint(screen, f"Number of buttons: {buttons}")
            text_print.indent()

            for i in range(buttons):
                button = joystick.get_button(i)
                text_print.tprint(screen, f"Button {i:>2} value: {button}")
            text_print.unindent()

            hats = joystick.get_numhats()
            text_print.tprint(screen, f"Number of hats: {hats}")
            text_print.indent()

            # Положение шляпы. Все или ничего для направления, а не поплавок, как
            # get_axis(). Position — это кортеж значений int (x, y).
            for i in range(hats):
                hat = joystick.get_hat(i)
                text_print.tprint(screen, f"Hat {i} value: {str(hat)}")
            text_print.unindent()

            text_print.unindent()

        # Продолжаем и обновляем экран тем, что мы нарисовали.
        pygame.display.flip()

        # Ограничение до 30 кадров в секунду.
        clock.tick(30)


if __name__ == "__main__":
    main()
    # Если вы забудете эту строку, программа «зависнет»
    # при выходе из режима IDLE.
    pygame.quit()