import tkinter as tk

class TodoView:
    def __init__(self):
        self.root = tk.Tk()
        self.todo_lists = []

        # Création des widgets pour l'IHM
        self.todo_lists_frame = tk.Frame(self.root)
        self.todo_lists_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.todo_items_frame = tk.Frame(self.root)
        self.todo_items_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.todo_items_columns = [
            ("À faire", "red"),
            ("En cours", "orange"),
            ("Fait", "green")
        ]
        self.todo_item_columns_frames = []

        # Création de la vue pour les listes de tâches
        self.create_todo_list_view()

    def create_todo_list_view(self):
        todo_list_label = tk.Label(self.todo_lists_frame, text="Listes de tâches", font=("Helvetica", 16, "bold"))
        todo_list_label.pack()

        self.todo_lists_frame_inner = tk.Frame(self.todo_lists_frame)
        self.todo_lists_frame_inner.pack()

        for todo_list in self.todo_lists:
            todo_list_button = tk.Button(self.todo_lists_frame_inner, text=todo_list["name"], width=20, pady=10)
            todo_list_button.pack()

    def create_todo_item_view(self, todo_list_index):
        todo_item_frame = tk.Frame(self.todo_items_frame, relief=tk.RAISED, borderwidth=2)
        todo_item_frame.pack(pady=10)

        todo_list_title = tk.Label(todo_item_frame, text=self.todo_lists[todo_list_index]["name"], font=("Helvetica", 14, "bold"))
        todo_list_title.pack()

        todo_item_form_frame = tk.Frame(todo_item_frame)
        todo_item_form_frame.pack(pady=10)

        # TODO: Ajouter les widgets pour saisir les détails d'une tâche (titre, description, priorité, date limite)

        todo_items_frame = tk.Frame(todo_item_frame)
        todo_items_frame.pack()

        for column_name, column_color in self.todo_items_columns:
            column_frame = tk.Frame(todo_items_frame, relief=tk.RAISED, borderwidth=2)
            column_frame.pack(side=tk.LEFT, padx=10)

            column_title = tk.Label(column_frame, text=column_name, font=("Helvetica", 12, "bold"))
            column_title.pack(pady=5)

            # TODO: Ajouter les widgets pour afficher les tâches correspondantes à chaque colonne

            self.todo_item_columns_frames.append(column_frame)

    def update_todo_lists(self, todo_lists):
        self.todo_lists = todo_lists

        # Effacer les anciens boutons des listes de tâches
        for widget in self.todo_lists_frame_inner.winfo_children():
            widget.destroy()

        # Recréer les boutons avec les nouvelles listes de tâches
        for todo_list in self.todo_lists:
            todo_list_button = tk.Button(self.todo_lists_frame_inner, text=todo_list["name"], width=20, pady=10)
            todo_list_button.pack()

    def update_todo_items(self, todo_list_index, todo_items):
        # Effacer les anciens widgets des tâches
        for frame in self.todo_item_columns_frames:
            for widget in frame.winfo_children():
                widget.destroy()

        # Recréer les widgets pour afficher les nouvelles tâches
        for todo_item in todo_items:
            # TODO: Créer les widgets pour afficher les détails d'une tâche dans la colonne appropriée

    def run(self):
        self.root.mainloop()