# Neuro-Bools-and-Neuro-Cows
Это простенькая на первый вид игра написанная на Python. Мною был создан движок для генерации четырёхзначного числа, цифры которого всегда будут разными

Это учебный проект. Я использовал чистый python, библиотеки tkinter для отрисовки интерфейса, subprocess для работы с движком генератора, 
random для получения сида генератора.

Генератор работает следующим образом:
 -Программа начинается с импорта модуля random для генерации случайных чисел. Затем определяются четыре класса: Neuron1, Neuron2, Neuron3 и Neuron4. Каждый класс представляет собой нейрон и содержит методы для     
 инициализации нейрона случайными весами, активации нейрона с набором входных данных и генерации выходных данных на основе активации.
 Далее создаются экземпляры Neuron1, Neuron2, Neuron3 и Neuron4, и их методы generate_output вызываются для получения четырех чисел (num1, num2, num3, num4).
 Для гарантирования уникальности сгенерированных чисел определяется функция make_numbers_different. Она проходит по числам и увеличивает или уменьшает их, если есть дубликаты, пока все числа не станут 
 уникальными.
 Затем функция make_numbers_different вызывается с четырьмя сгенерированными числами, и результат сохраняется в переменной result.
 Также определяется еще один класс под названием Neuron. У этого класса есть методы для инициализации нейрона, активации с входными данными и обработки входных данных специфическим образом.
 Создается экземпляр Neuron, и его методы вызываются для обработки входных данных. Результат возвращается в основной программе.

Программа скомпилирована в exe для удобства, портировать под другие ОС не планируется.

Разработчик: Urban Egor
Страна: Российская Федерация
Год: 2022-2023
Версия: 2.2.56 RBA

#Версии обозначаются следующим образом: "A.X.Y COD" где A - Релизная версия, X - Бета версия, Y - Альфа версия, COD - Какие тесты прошла программа(R-ПредРелизный тест, B-Бета тест, A-АльфаТест)
 В данном случае это второе релищное обновление, втарая бетка, и 56 альфа-запуск. Программа прошла все этапы тестов.

P.S. В игре не используются нейронные сети, всего лишь псевдослучайная генерация числа со случаными параметрами подбора
