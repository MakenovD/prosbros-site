# Extra copy for the v2 design. Chat lines customers see stay in English on purpose.

CHAT = [  # (who, text) — hero phone animation
    ('c', 'Hi! Still need the bathroom fan swapped. How much?'),
    ('b', "Hey Sarah! Yep, I can do it. Fan swap is $180, parts included. I've got Tue 9am or Wed 2pm — which works?"),
    ('c', 'Sounds good, $180 works. Tuesday?'),
    ('b', "Done ✅ Tuesday 9am. See you then!"),
]

DEMO = [  # (question, answer) — "Ask Bro" demo, example prices
    ('How much to mount a 65" TV?', 'Mounting a 65" TV is $149 with the bracket install. Hiding the cables in the wall is +$60. I can come Thu 4pm or Sat 10am — want me to lock one in?'),
    ('Are you free this Saturday?', "Saturday I've got 10am or 1pm open. What's the job and your ZIP? I'll confirm the price before I come out."),
    ('Can you do it cheaper?', 'My prices are fair and fixed — no surprise fees. If you bundle 2+ small jobs in one visit, I take $25 off. Want to add something?'),
    ('Do you haul away the old stuff?', "Yep — haul-away is $40 for small items, $90 for a full truck bed. I'll put it in the quote so you see the total upfront."),
]

PHOTOS = dict(
    hero='photo-1505798577917-a65157d3320a',
    handyman='photo-1765518440022-10242cc86895',
    cleaning='photo-1686178827149-6d55c72d81df',
    moving='photo-1694715669993-ea0022b470f7',
    painting='photo-1717281234297-3def5ae3eee1',
    plumbing='photo-1676210134188-4c05dd172f89',
    electrical='photo-1682345262055-8f95f3c513ea',
)

EXTRA = {
 'en': dict(
    badge='Built for Thumbtack pros', h1_hl='dead leads', cta2='See it answer',
    phone_name='Sarah · Bathroom fan swap', phone_status='Bro is answering for you…', phone_input='Message',
    notif_t='New job booked', notif_d='$180 · Tue 9:00 AM · Sarah',
    chip1='Replied in 38 sec', chip2='Old lead woke up', chip3='+$180 booked',
    trades_h='For every trade on Thumbtack', trades=['Handyman', 'Cleaning', 'Moving', 'Painting', 'Plumbing', 'Electrical'], trades_more='+ 500 more services',
    case_label='The inbox after our test', case_cap='Real messages from one handyman’s Thumbtack inbox. Names left out.',
    demo_eyebrow='Try it', demo_h2='Ask Bro like a customer would',
    demo_p='Tap a question. Bro answers the way you would — your prices, your schedule, your tone.',
    demo_you='Customer', demo_bro='Bro · in your name', demo_typing='typing…',
    demo_note='Customers write in English, so Bro answers in English. Example prices — Bro uses yours.',
    demo_start='Pick a question to see the answer →', demo_cta='I want this on my leads',
    steps_label='Step',
 ),
 'es': dict(
    badge='Hecho para pros de Thumbtack', h1_hl='leads muertos', cta2='Míralo contestar',
    phone_name='Sarah · Cambio de extractor', phone_status='Bro está contestando por ti…', phone_input='Mensaje',
    notif_t='Nuevo jale agendado', notif_d='$180 · mar 9:00 AM · Sarah',
    chip1='Contestó en 38 seg', chip2='Lead viejo revivió', chip3='+$180 agendado',
    trades_h='Para todos los oficios en Thumbtack', trades=['Handyman', 'Limpieza', 'Mudanzas', 'Pintura', 'Plomería', 'Electricidad'], trades_more='+ 500 servicios más',
    case_label='Así quedó el inbox después de la prueba', case_cap='Mensajes reales del inbox de Thumbtack de un handyman. Sin nombres.',
    demo_eyebrow='Pruébalo', demo_h2='Pregúntale a Bro como lo haría un cliente',
    demo_p='Toca una pregunta. Bro contesta como tú — con tus precios, tu horario y tu forma de hablar.',
    demo_you='Cliente', demo_bro='Bro · a tu nombre', demo_typing='escribiendo…',
    demo_note='Los clientes escriben en inglés, así que Bro contesta en inglés. Precios de ejemplo — Bro usa los tuyos.',
    demo_start='Escoge una pregunta para ver la respuesta →', demo_cta='Lo quiero para mis leads',
    steps_label='Paso',
 ),
 'ru': dict(
    badge='Для мастеров на Thumbtack', h1_hl='мёртвые лиды', cta2='Посмотреть, как отвечает',
    phone_name='Sarah · Замена вытяжки', phone_status='Bro отвечает за тебя…', phone_input='Сообщение',
    notif_t='Новый заказ записан', notif_d='$180 · вт 9:00 · Sarah',
    chip1='Ответил за 38 сек', chip2='Старый лид ожил', chip3='+$180 записано',
    trades_h='Для любых мастеров на Thumbtack', trades=['Хендимен', 'Клининг', 'Мувинг', 'Покраска', 'Сантехника', 'Электрика'], trades_more='+ ещё 500 услуг',
    case_label='Так выглядел инбокс после теста', case_cap='Реальные сообщения из Thumbtack-инбокса хендимена. Имена скрыты.',
    demo_eyebrow='Попробуй', demo_h2='Спроси Bro, как спросил бы кастомер',
    demo_p='Нажми на вопрос. Bro отвечает так, как ответил бы ты: твои цены, твоё расписание, твой тон.',
    demo_you='Кастомер', demo_bro='Bro · от твоего имени', demo_typing='печатает…',
    demo_note='Кастомеры пишут по-английски, поэтому Bro отвечает по-английски. Цены для примера — Bro берёт твои.',
    demo_start='Выбери вопрос, чтобы увидеть ответ →', demo_cta='Хочу так на свои лиды',
    steps_label='Шаг',
 ),
 'uk': dict(
    badge='Для майстрів на Thumbtack', h1_hl='мертві ліди', cta2='Подивитись, як відповідає',
    phone_name='Sarah · Заміна витяжки', phone_status='Bro відповідає за тебе…', phone_input='Повідомлення',
    notif_t='Нове замовлення записано', notif_d='$180 · вт 9:00 · Sarah',
    chip1='Відповів за 38 сек', chip2='Старий лід ожив', chip3='+$180 записано',
    trades_h='Для будь-яких майстрів на Thumbtack', trades=['Хендімен', 'Клінінг', 'Мувінг', 'Фарбування', 'Сантехніка', 'Електрика'], trades_more='+ ще 500 послуг',
    case_label='Так виглядав інбокс після тесту', case_cap='Справжні повідомлення з Thumbtack-інбоксу хендимена. Імена приховано.',
    demo_eyebrow='Спробуй', demo_h2='Запитай Bro, як запитав би кастомер',
    demo_p='Натисни на питання. Bro відповідає так, як відповів би ти: твої ціни, твій розклад, твій тон.',
    demo_you='Кастомер', demo_bro='Bro · від твого імені', demo_typing='друкує…',
    demo_note='Кастомери пишуть англійською, тому Bro відповідає англійською. Ціни для прикладу — Bro бере твої.',
    demo_start='Обери питання, щоб побачити відповідь →', demo_cta='Хочу так на свої ліди',
    steps_label='Крок',
 ),
}
