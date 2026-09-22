from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ApplioMobileApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
    title_label = Label(
        text='Applio Mobile Interface',
        font_size=24,
        size_hint_y=None,
        height=50,
    )
    status_label = Label(
        text='Initialized successfully!\nReady for voice conversion pipelines.',
        font_size=16,
    )

    layout.add_widget(title_label)
    layout.add_widget(status_label)
    return layout


if __name__ == '__main__':
  ApplioMobileApp().run()

