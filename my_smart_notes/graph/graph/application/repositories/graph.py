import abc


class GraphRepository(abc.ABC):

    @abc.abstractmethod
    def create_tag_node(self, note_id):
        pass

    @abc.abstractmethod
    def remove_tag_node(self, note_id):
        pass

    @abc.abstractmethod
    def create_note_node(self, tag_id):
        pass

    @abc.abstractmethod
    def remove_note_node(self, note_id):
        pass

    @abc.abstractmethod
    def create_relationship_from_note_to_tag(self, note_id, tag_id):
        pass

    @abc.abstractmethod
    def remove_relationship_from_note_to_tag(self, note_id, tag_id):
        pass
