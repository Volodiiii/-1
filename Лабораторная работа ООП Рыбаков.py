import doctest

class Table:
    def __init__(self, material: str, width: float, length: float):
        """
        Инициализирует объект "Стол" с материалом, шириной и длиной.

        :param material: Тип материала, из которого сделан стол
        :param width: Ширина стола в метрах
        :param length: Длина стола в метраx
        """
        if width <= 0 or length <= 0:
            raise ValueError("Ширина и длина стола должны быть больше нуля.")

        self.material = material
        self.width = width
        self.length = length

    def calculate_area(self) -> float:
        """
        Метод для расчета площади стола.

        :return: Площадь стола в квадратных метрах.
        """
        return self.width * self.length

    def set_material(self, material: str) -> None:
        """
        Устанавливает новый материал стола.

        :material: Новый материал для стола.
        :return: None

        Примеры
        >>> table = Table("дерево", 2, 3)
        >>> table.set_material("металл")
        >>> table.material
        'металл'
        """
        ...


class OnlineLearningPlatform:
    def __init__(self, platform_name: str, user_count: int, launch_year: int):
        """
        Платформа для онлайн-обучения с названием, количеством пользователей и годом запуска.

        platform_name Название платформы.
        user_count Количество пользователей платформы, должно быть положительным числом.
        launch_year: Год запуска платформы.

        """

        if not platform_name:
            raise ValueError("Название платформы не может быть пустым.")
        if user_count <= 0:
            raise ValueError("Количество пользователей должно быть положительным числом.")
        if launch_year < 2000:
            raise ValueError("Платформа должна быть запущена после 2000 года.")

        self.platform_name = platform_name
        self.user_count = user_count
        self.launch_year = launch_year

    def enroll_student(self, student_name: str) -> None:
        """
        Метод для записи нового студента на платформу.

        :student_name: Имя студента.
        :return: None
        :raises ValueError: Если имя студента пустое.

        Пример:
        >>> platform = Coursera("Coursera", 1000000, 2012)
        >>> platform.enroll_student("Иван")
        """
        ...

    def start_course(self, course_name: str) -> None:
        """
        Метод для запуска курса на платформе.

        :course_name: Название курса.
        :return: None
        :raises ValueError: Если название курса пустое.

        Пример:
        >>> platform = Coursera("Coursera", 1000000, 2012)
        >>> platform.start_course("Python для начинающих")
        """
        ...


    class Car(ABC):
        def __init__(self, brand: str, model: str, year: int):
            """
            Автомобиль с маркой, моделью и годом выпуска.

            :brand: Марка автомобиля (например, "Toyota").
            :model: Модель автомобиля (например, "Corolla").
            :year: Год выпуска автомобиля, должен быть не меньше текущего года.

            :raises ValueError: Если год выпуска автомобиля меньше 1886 (первый автомобиль был создан в 1886 году).
            """
            if not brand:
                raise ValueError("Марка автомобиля не может быть пустой.")
            if not model:
                raise ValueError("Модель автомобиля не может быть пустой.")
            if year < 1886:
                raise ValueError("Год выпуска автомобиля не может быть меньше 1886.")

            self.brand = brand
            self.model = model
            self.year = year

        def start_engine(self) -> None:
            """
            Метод для запуска двигателя автомобиля.

            :return: None
            Пример:
            >>> car = Sedan("Toyota", "Camry", 2020)
            >>> car.start_engine()
            """
            ...

        def drive(self, distance: float) -> None:
            """
            Метод для движения автомобиля на заданное расстояние.

            :param distance: Расстояние в километрах.
            :return: None
            :raises ValueError: Если расстояние меньше или равно 0.

            Пример:
            >>> car = Sedan("Toyota", "Camry", 2020)
            >>> car.drive(100)
            """
            ...