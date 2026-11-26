# v3 copy: changes from the Schwartz / Great Leads review, applied on top of the v2 copy.
# One big idea: you already paid for these jobs, Bro goes back and gets them ("Second Shot").
import copy
from i18n import EN, LANGS
from i18n_extra import EXTRA

P = {
 'en': dict(
    title='ProsBros — Get back the Thumbtack jobs you already paid for',
    desc="ProsBros goes back through your old Thumbtack chats, gets customers talking again and hands you the ones ready to book — your prices, your words, your OK. For handymen, cleaners, movers and other home-service pros.",
    h1='You already paid for these jobs. We get them back.',
    sub="Bro reopens your old Thumbtack chats, gets customers talking again, and hands you the ones ready to book. Your prices. Your words. Your OK.",
    bridge='So every quiet chat in your inbox is money you already spent.',
    pilot_p="An LA handyman paid for every one of those leads and answered what he could between jobs. We texted 493 of his old customers and leads. 19 wrote back, 15 with a real job — and 12 of them never heard back, because he was busy on jobs. That's why Bro does both: brings customers back <em>and</em> keeps the conversation going till the job's on your calendar.",
    how_h2='How Second Shot works',
    how=[('Sorts your inbox into 4 piles', "Connect on Thumbtack's own page — we never see your password. Bro sorts your old chats: asked a price and vanished · said yes but never set a day · went with another pro · never got an answer."),
         ('Writes each pile its own message', 'No “just checking in.” Bro writes about their job: “Still need that shelf mounted? I’ve got Tuesday open.” You OK the first batch before anything goes out.'),
         ('Answers in your words, at your prices', 'Customers write back with questions. Bro answers from your rate sheet and calendar. Discounts and custom work come to you.'),
         ('Hands you the ones ready to book', 'The second a customer agrees on a price or picks a day, you get a text. You confirm — the job is yours.')],
    safe="<b>Can this get my Thumbtack account in trouble?</b> You sign in on Thumbtack's own page and can disconnect anytime. No password, no bots — Thumbtack's official connection for partner apps (approval in progress).",
    feat=[('Second Shot: old leads come back', 'A short, personal note to past customers and quiet quotes — about their job, with your name. Past customers first: they answer 2.5× more.'),
          ('First Reply: new leads answered in minutes', "Day or night, in your words, while you're on a job. Quotes only your rates — never makes up a price. Follows up after 2 hours, the next day and in 3 days."),
          ("Texts you when it's ready to book", 'Get a text (or WhatsApp / Telegram) the moment a customer agrees on a price or picks a time. You take it from there.'),
          ("Won't make you look bad", 'No double messages. No canned text in the middle of a price talk. Same customer once a quarter, max. Stops the second you jump in.')],
    cmp_h2='Other ways to keep up — and where they fall short',
    cmp_cols=['Auto-reply apps', 'Someone on the phone', 'ProsBros'],
    cmp_rows=[('Answers new leads fast', 'Same canned text', "When they're free", 'In minutes, in your words'),
              ('Goes back to your old Thumbtack leads', 'No', 'Rarely', 'Yes — every old chat'),
              ('Quotes only your prices', 'Usually not', 'After you train them', 'Yes — from your rate sheet'),
              ("Hands you the customer when they're ready to book", 'Sometimes', 'Yes', 'Yes'),
              ('What it costs', '$29–99 / mo', '$15–20 / hour', '$149–249 / mo')],
    price_p='At $25–75 a lead, $249 is the price of 4–10 Thumbtack leads. Start with a free inbox check. No contract — cancel anytime. Pay for the year, get 2 months free.',
    plan_names=['Inbox Check', 'Second Shot', 'Second Shot + First Reply', 'Crew'],
    free_items=['Customers who never got an answer', 'Quotes that went quiet', 'What those jobs are worth at your prices', 'First 100 old leads, free for 14 days'],
    free_cta='Check my inbox',
    p1_first='Win back the leads you already paid for — every old chat + a fresh batch each month',
    p2_first='Everything in Second Shot', p3_first='Everything in Second Shot + First Reply',
    faq_add=[('Is this AI?', "Yes — Bro is software set up with your prices and rules. It writes in your name, and anything it isn't sure about comes to you."),
             ("How do I know it's working?", 'You see messages sent, answers, jobs booked and dollars in. Log a job amount with one tap.')],
    audit_h2="See what's hiding in your inbox",
    audit_p="Ready minutes after you connect: who never got an answer, which quotes went quiet, and what those jobs are worth at your prices. Why free? If there's nothing to win back, we'll tell you straight. We set up every pro by hand, so spots open in small batches.",
 ),
 'es': dict(
    title='ProsBros — Recupera los jales de Thumbtack que ya pagaste',
    desc='ProsBros revisa tus pláticas viejas de Thumbtack, vuelve a sacarles plática a los clientes y te pasa los que ya quieren agendar — con tus precios, tus palabras y tu OK. Para handymen, limpieza, mudanzas y todos los pros.',
    h1='Ya pagaste estos jales. Nosotros te los regresamos.',
    sub='Bro reabre tus pláticas viejas de Thumbtack, vuelve a sacarles plática a los clientes y te pasa los que ya quieren agendar. Tus precios. Tus palabras. Tu OK.',
    bridge='O sea: cada plática callada en tu inbox es lana que ya gastaste.',
    pilot_p='Un handyman de LA pagó cada uno de esos leads y contestaba lo que podía entre jale y jale. Le textearon a 493 de sus clientes y leads viejos. 19 contestaron, 15 con un jale de verdad — y a 12 de ellos nadie les respondió, porque él andaba trabajando. Por eso Bro hace las dos cosas: trae de vuelta a los clientes <em>y</em> sigue la plática hasta que el jale queda en tu calendario.',
    how_h2='Cómo funciona Second Shot',
    how=[('Separa tu inbox en 4 montones', 'Conectas en la página oficial de Thumbtack — nunca vemos tu password. Bro acomoda tus pláticas viejas: preguntó precio y desapareció · dijo que sí pero nunca puso fecha · se fue con otro pro · nadie le contestó.'),
         ('Le escribe a cada montón su propio mensaje', 'Nada de “solo para saber”. Bro les escribe de su jale: “¿Todavía necesitas la repisa? Tengo libre el martes.” Tú das el OK a la primera tanda antes de que salga algo.'),
         ('Contesta con tus palabras y tus precios', 'Los clientes contestan con preguntas. Bro responde con tu lista de precios y tu calendario. Descuentos y trabajos especiales te llegan a ti.'),
         ('Te pasa los que ya quieren agendar', 'En cuanto un cliente acepta el precio o escoge día, te llega un texto. Tú confirmas — el jale es tuyo.')],
    safe='<b>¿Me pueden bloquear la cuenta de Thumbtack por esto?</b> Entras en la página oficial de Thumbtack y nos desconectas cuando quieras. Sin password, sin bots — la conexión oficial de Thumbtack para apps socias (la aprobación va en proceso).',
    feat=[('Second Shot: los leads viejos regresan', 'Un mensajito corto y personal a clientes de antes y cotizaciones que se enfriaron — de su jale, con tu nombre. Primero los clientes de antes: contestan 2.5× más.'),
          ('First Reply: leads nuevos contestados en minutos', 'De día o de noche, con tus palabras, mientras estás en el jale. Solo da tus precios — nunca se inventa uno. Da seguimiento a las 2 horas, al otro día y a los 3 días.'),
          ('Te textea cuando ya quieren agendar', 'Te llega un texto (o WhatsApp / Telegram) en cuanto un cliente acepta el precio o escoge hora. De ahí sigues tú.'),
          ('No te hace quedar mal', 'Sin mensajes dobles. Nada de textos de plantilla a media negociación. Al mismo cliente, máximo una vez cada tres meses. Se para en cuanto tú contestas.')],
    cmp_h2='Otras formas de darse abasto — y dónde se quedan cortas',
    cmp_cols=['Apps de respuesta automática', 'Alguien en el teléfono', 'ProsBros'],
    cmp_rows=[('Contesta leads nuevos rápido', 'El mismo texto de plantilla', 'Cuando tiene tiempo', 'En minutos, con tus palabras'),
              ('Va por tus leads viejos de Thumbtack', 'No', 'Casi nunca', 'Sí — cada plática vieja'),
              ('Solo da tus precios', 'Casi nunca', 'Después de que lo entrenes', 'Sí — de tu lista de precios'),
              ('Te pasa al cliente cuando ya quiere agendar', 'A veces', 'Sí', 'Sí'),
              ('Cuánto cuesta', '$29–99 / mes', '$15–20 / hora', '$149–249 / mes')],
    price_p='A $25–75 por lead, $249 es lo que cuestan 4–10 leads de Thumbtack. Empieza con una revisión gratis de tu inbox. Sin contrato — cancelas cuando quieras. Pagas el año y te regalamos 2 meses.',
    plan_names=['Revisión del inbox', 'Second Shot', 'Second Shot + First Reply', 'Crew'],
    free_items=['Clientes a los que nadie les contestó', 'Cotizaciones que se enfriaron', 'Cuánto valen esos jales con tus precios', 'Primeros 100 leads viejos, gratis por 14 días'],
    free_cta='Checa mi inbox',
    p1_first='Recupera los leads que ya pagaste — cada plática vieja + una tanda nueva cada mes',
    p2_first='Todo lo de Second Shot', p3_first='Todo lo de Second Shot + First Reply',
    faq_add=[('¿Esto es AI?', 'Sí — Bro es un software configurado con tus precios y tus reglas. Escribe a tu nombre, y lo que no tiene claro te lo pasa a ti.'),
             ('¿Cómo sé que está funcionando?', 'Ves mensajes enviados, respuestas, jales agendados y la lana que entró. Apuntas cuánto salió un jale con un toque.')],
    audit_h2='Mira lo que tienes escondido en tu inbox',
    audit_p='Lista minutos después de conectar: a quién nadie le contestó, qué cotizaciones se enfriaron y cuánto valen esos jales con tus precios. ¿Por qué gratis? Si no hay nada que recuperar, te lo decimos derecho. Configuramos a cada pro a mano, por eso abrimos lugares en tandas chicas.',
 ),
 'ru': dict(
    title='ProsBros — верни заказы из Thumbtack, за которые ты уже заплатил',
    desc='ProsBros поднимает твои старые переписки в Thumbtack, заново заводит разговор с кастомерами и передаёт тебе тех, кто готов записаться — по твоим ценам, твоими словами, с твоего ОК. Для хендименов, клининга, мувинга и других мастеров.',
    h1='Ты уже заплатил за эти заказы. Мы их вернём.',
    sub='Bro поднимает твои старые переписки в Thumbtack, заново заводит разговор с кастомерами и передаёт тебе тех, кто готов записаться. Твои цены. Твои слова. Твоё ОК.',
    bridge='То есть каждая заглохшая переписка в инбоксе — это бабки, которые ты уже потратил.',
    pilot_p='Хендимен из LA платил за каждый из этих лидов и отвечал, когда успевал между заказами. Мы написали 493 его старым кастомерам и лидам. 19 ответили, 15 — с реальным заказом, и 12 из них так и не дождались ответа: он был на объектах. Поэтому Bro делает и то, и другое: возвращает кастомеров <em>и</em> ведёт переписку, пока заказ не встанет тебе в календарь.',
    how_h2='Как работает Second Shot',
    how=[('Раскладывает инбокс на 4 стопки', 'Подключаешься на странице самого Thumbtack — пароль мы не видим. Bro разбирает старые переписки: спросил цену и пропал · согласился, но день не назначили · ушёл к другому мастеру · ему так никто и не ответил.'),
         ('Пишет каждой стопке своё', 'Никаких «просто уточняю». Bro пишет про их заказ: «Полку над телеком ещё надо повесить? Во вторник есть окно». Первую партию ты одобряешь до отправки.'),
         ('Отвечает твоими словами, по твоим ценам', 'Кастомеры отвечают с вопросами. Bro отвечает по твоему прайсу и календарю. Скидки и нестандартные работы — к тебе.'),
         ('Передаёт тех, кто готов записаться', 'Как только кастомер согласился на цену или выбрал день — тебе приходит текст. Подтверждаешь — заказ твой.')],
    safe='<b>Не забанят мой аккаунт в Thumbtack?</b> Ты входишь на странице самого Thumbtack и можешь отключить нас в любой момент. Без пароля, без ботов — официальное подключение Thumbtack для партнёрских приложений (одобрение в процессе).',
    feat=[('Second Shot: старые лиды возвращаются', 'Короткое личное сообщение старым кастомерам и заглохшим эстимейтам — про их заказ, с твоим именем. Сначала старые кастомеры: они отвечают в 2,5× чаще.'),
          ('First Reply: новым лидам — ответ за минуты', 'Днём и ночью, твоими словами, пока ты на объекте. Называет только твои цены — ничего не выдумывает. Дожимает через 2 часа, на следующий день и через 3 дня.'),
          ('Кидает тебе текст, когда кастомер готов', 'Текст (или WhatsApp / Telegram), как только кастомер согласился на цену или выбрал время. Дальше — ты.'),
          ('Не подставит тебя', 'Без дублей. Без шаблонов посреди торга. Одному кастомеру — не чаще раза в квартал. Отваливает, как только ты подключился.')],
    cmp_h2='Как ещё мастера пытаются успевать — и где это не работает',
    cmp_cols=['Автоответчики', 'Человек на телефоне', 'ProsBros'],
    cmp_rows=[('Быстро отвечает новым лидам', 'Один и тот же шаблон', 'Когда свободен', 'За минуты, твоими словами'),
              ('Возвращает старые лиды из Thumbtack', 'Нет', 'Редко', 'Да — каждую старую переписку'),
              ('Называет только твои цены', 'Обычно нет', 'После того, как обучишь', 'Да — из твоего прайса'),
              ('Передаёт кастомера, когда он готов записаться', 'Иногда', 'Да', 'Да'),
              ('Сколько стоит', '$29–99 / мес', '$15–20 / час', '$149–249 / мес')],
    price_p='При $25–75 за лид $249 — это цена 4–10 лидов в Thumbtack. Начни с бесплатной проверки инбокса. Без контракта — отменить можно в любой момент. Платишь за год — 2 месяца в подарок.',
    plan_names=['Проверка инбокса', 'Second Shot', 'Second Shot + First Reply', 'Crew'],
    free_items=['Кастомеры, которым так никто и не ответил', 'Эстимейты, которые заглохли', 'Сколько стоят эти заказы по твоим ценам', 'Первые 100 старых лидов — бесплатно 14 дней'],
    free_cta='Проверить инбокс',
    p1_first='Возвращаем лиды, за которые ты уже заплатил — каждую старую переписку + свежая партия каждый месяц',
    p2_first='Всё из Second Shot', p3_first='Всё из Second Shot + First Reply',
    faq_add=[('Это AI?', 'Да — Bro это программа, настроенная под твои цены и правила. Пишет от твоего имени, а всё, в чём не уверен, передаёт тебе.'),
             ('Как понять, что это работает?', 'Видно, сколько написали, сколько ответили, сколько заказов записалось и сколько долларов пришло. Сумму за заказ — в одно касание.')],
    audit_h2='Посмотри, что лежит у тебя в инбоксе',
    audit_p='Готово через пару минут после подключения: кому так никто и не ответил, какие эстимейты заглохли и сколько стоят эти заказы по твоим ценам. Почему бесплатно? Если возвращать нечего — так прямо и скажем. Каждого мастера настраиваем вручную, поэтому открываем места небольшими партиями.',
 ),
 'uk': dict(
    title='ProsBros — поверни замовлення з Thumbtack, за які ти вже заплатив',
    desc='ProsBros піднімає твої старі переписки в Thumbtack, знову заводить розмову з кастомерами й передає тобі тих, хто готовий записатися — за твоїми цінами, твоїми словами, з твого ОК. Для хендименів, клінінгу, мувінгу та інших майстрів.',
    h1='Ти вже заплатив за ці замовлення. Ми їх повернемо.',
    sub='Bro піднімає твої старі переписки в Thumbtack, знову заводить розмову з кастомерами й передає тобі тих, хто готовий записатися. Твої ціни. Твої слова. Твоє ОК.',
    bridge='Тобто кожна заглухла переписка в інбоксі — це кеш, який ти вже витратив.',
    pilot_p='Хендимен із LA платив за кожен із цих лідів і відповідав, коли встигав між замовленнями. Ми написали 493 його старим кастомерам і лідам. 19 відповіли, 15 — зі справжнім замовленням, і 12 із них так і не дочекалися відповіді: він був на об’єктах. Тому Bro робить і те, й інше: повертає кастомерів <em>і</em> веде переписку, поки замовлення не стане тобі в календар.',
    how_h2='Як працює Second Shot',
    how=[('Розкладає інбокс на 4 стоси', 'Підключаєшся на сторінці самого Thumbtack — пароль ми не бачимо. Bro розбирає старі переписки: спитав ціну й зник · погодився, але день не призначили · пішов до іншого майстра · йому так ніхто й не відповів.'),
         ('Пише кожному стосу своє', 'Жодних «просто уточнюю». Bro пише про їхнє замовлення: «Полицю над телеком ще треба повісити? У вівторок є вікно». Першу партію ти схвалюєш до відправки.'),
         ('Відповідає твоїми словами, за твоїми цінами', 'Кастомери відповідають із питаннями. Bro відповідає за твоїм прайсом і календарем. Знижки та нестандартні роботи — до тебе.'),
         ('Передає тих, хто готовий записатися', 'Щойно кастомер погодився на ціну чи обрав день — тобі приходить текст. Підтверджуєш — замовлення твоє.')],
    safe='<b>Чи не заблокують мій акаунт у Thumbtack?</b> Ти входиш на сторінці самого Thumbtack і можеш відключити нас будь-коли. Без пароля, без ботів — офіційне підключення Thumbtack для партнерських застосунків (схвалення в процесі).',
    feat=[('Second Shot: старі ліди повертаються', 'Коротке особисте повідомлення старим кастомерам і заглухлим естимейтам — про їхнє замовлення, з твоїм іменем. Спершу старі кастомери: вони відповідають у 2,5× частіше.'),
          ('First Reply: новим лідам — відповідь за хвилини', 'Удень і вночі, твоїми словами, поки ти на об’єкті. Називає лише твої ціни — нічого не вигадує. Дотискає через 2 години, наступного дня й через 3 дні.'),
          ('Кидає тобі текст, коли кастомер готовий', 'Текст (або WhatsApp / Telegram), щойно кастомер погодився на ціну чи обрав час. Далі — ти.'),
          ('Не підставить тебе', 'Без дублів. Без шаблонів посеред торгу. Одному кастомеру — не частіше ніж раз на квартал. Відстає, щойно ти підключився.')],
    cmp_h2='Як ще майстри намагаються встигати — і де це не працює',
    cmp_cols=['Автовідповідачі', 'Людина на телефоні', 'ProsBros'],
    cmp_rows=[('Швидко відповідає новим лідам', 'Один і той самий шаблон', 'Коли вільна', 'За хвилини, твоїми словами'),
              ('Повертає старі ліди з Thumbtack', 'Ні', 'Рідко', 'Так — кожну стару переписку'),
              ('Називає лише твої ціни', 'Зазвичай ні', 'Після того, як навчиш', 'Так — із твого прайсу'),
              ('Передає кастомера, коли він готовий записатися', 'Іноді', 'Так', 'Так'),
              ('Скільки коштує', '$29–99 / міс', '$15–20 / год', '$149–249 / міс')],
    price_p='При $25–75 за лід $249 — це ціна 4–10 лідів у Thumbtack. Почни з безкоштовної перевірки інбоксу. Без контракту — скасувати можна будь-коли. Платиш за рік — 2 місяці в подарунок.',
    plan_names=['Перевірка інбоксу', 'Second Shot', 'Second Shot + First Reply', 'Crew'],
    free_items=['Кастомери, яким так ніхто й не відповів', 'Естимейти, що заглухли', 'Скільки коштують ці замовлення за твоїми цінами', 'Перші 100 старих лідів — безкоштовно 14 днів'],
    free_cta='Перевірити інбокс',
    p1_first='Повертаємо ліди, за які ти вже заплатив — кожну стару переписку + свіжа партія щомісяця',
    p2_first='Усе з Second Shot', p3_first='Усе з Second Shot + First Reply',
    faq_add=[('Це AI?', 'Так — Bro це програма, налаштована під твої ціни й правила. Пише від твого імені, а все, у чому не впевнений, передає тобі.'),
             ('Як зрозуміти, що це працює?', 'Видно, скільки написали, скільки відповіли, скільки замовлень записалося і скільки доларів прийшло. Суму за замовлення — в один дотик.')],
    audit_h2='Подивись, що лежить у твоєму інбоксі',
    audit_p='Готово за пару хвилин після підключення: кому так ніхто й не відповів, які естимейти заглухли і скільки коштують ці замовлення за твоїми цінами. Чому безкоштовно? Якщо повертати нічого — так прямо й скажемо. Кожного майстра налаштовуємо вручну, тому відкриваємо місця невеликими партіями.',
 ),
}

HL = {'en': 'already paid', 'es': 'Ya pagaste', 'ru': 'уже заплатил', 'uk': 'вже заплатив'}

SIMPLE = ['title', 'desc', 'h1', 'sub', 'bridge', 'pilot_p', 'how_h2', 'how', 'safe', 'feat',
          'cmp_h2', 'cmp_cols', 'cmp_rows', 'price_p', 'audit_h2', 'audit_p']


def apply():
    for L in LANGS:
        p = P[L['code']]
        for k in SIMPLE:
            L[k] = p[k]
        plans = copy.deepcopy(L['plans'])
        for pl, n in zip(plans, p['plan_names']):
            pl['name'] = n
        plans[0]['items'] = p['free_items']
        plans[0]['cta'] = p['free_cta']
        plans[1]['items'][0] = p['p1_first']
        plans[2]['items'][0] = p['p2_first']
        plans[3]['items'][0] = p['p3_first']
        L['plans'] = plans
        # the account-safety question moves up next to the demo; two new questions join the FAQ
        L['faq'] = L['faq'][1:] + p['faq_add']
        EXTRA[L['code']]['h1_hl'] = HL[L['code']]
        assert HL[L['code']] in L['h1']
